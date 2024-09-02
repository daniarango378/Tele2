import asyncio
from aiohttp import web
from threading import Thread
from concurrent import futures
import grpc
import nod_pb2
import nod_pb2_grpc
import os
from dotenv import load_dotenv

# Load variables from .env file
load_dotenv()

# Define the path to the "files" directory
files_directory = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'files')

# Get configuration from .env file
grpc_port = os.getenv('GRPC_PORT')
rest_port = os.getenv('REST_PORT')
next_node_ip = os.getenv('NEXT_NODE_IP')
next_node_port = os.getenv('NEXT_NODE_PORT')
next_node = f"{next_node_ip}:{next_node_port}"
local_ip = os.getenv('LOCAL_IP')  # Add LOCAL_IP to .env file


class NodeService(nod_pb2_grpc.NodeServiceServicer):
    def __init__(self, service_port, next_node_address):
        self.service_port = service_port
        self.next_node_address = next_node_address

    def RequestFile(self, request, context):
        filename = request.filename
        origin_node = request.origin_node

        # Construct the full path of the requested file
        file_path = os.path.join(files_directory, filename)

        if os.path.isfile(file_path):
            # If the file is on this node, return its location
            return nod_pb2.FileResponse(content="", found=True, location=f"{local_ip}:{rest_port}")

        if origin_node == f"{local_ip}:{rest_port}":
            # If the file is not found and this is the original node of the request, return not found.
            return nod_pb2.FileResponse(content="", found=False, location="")

        # Propagate the request to the next node in the chain.
        try:
            with grpc.insecure_channel(self.next_node_address) as channel:
                stub = nod_pb2_grpc.NodeServiceStub(channel)
                response = stub.RequestFile(request)
                return response
        except grpc.RpcError as e:
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.UNAVAILABLE)
            return nod_pb2.FileResponse(content="", found=False, location="")

    def ListFiles(self, request, context):
        origin_node = request.origin_node

        # Get local files
        local_files = os.listdir(files_directory)
        all_files = set(local_files)

        if origin_node != f"{local_ip}:{rest_port}":
            # Propagate the file list request to the next node in the chain.
            try:
                with grpc.insecure_channel(self.next_node_address) as channel:
                    stub = nod_pb2_grpc.NodeServiceStub(channel)
                    response = stub.ListFiles(nod_pb2.ListFilesRequest(origin_node=origin_node))
                    all_files.update(response.files)
            except grpc.RpcError as e:
                context.set_details(str(e))
                context.set_code(grpc.StatusCode.UNAVAILABLE)

        return nod_pb2.ListFilesResponse(files=list(all_files))


def serve_grpc(port, next_node_address):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    nod_pb2_grpc.add_NodeServiceServicer_to_server(NodeService(port, next_node_address), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    print(f"gRPC server started on port {port}, next node: {next_node_address}")
    server.wait_for_termination()


async def search_file(request):
    filename = request.query.get('filename')
    if not filename:
        return web.json_response({"error": "Missing 'filename' parameter"}, status=400)

    # Check if the file is local
    file_path = os.path.join(files_directory, filename)
    if os.path.isfile(file_path):
        # If the file is local, return the download URL directly
        return web.json_response({
            "filename": filename,
            "download_url": f"http://{local_ip}:{rest_port}/download?filename={filename}"  # Use local_ip here
        }, status=200)

    # If the file is not local, use gRPC to request it from other nodes
    response = await asyncio.get_event_loop().run_in_executor(
        None, request_file_from_node, filename
    )

    if response.found:
        # Use the 'location' from the response to construct the download URL
        return web.json_response({
            "filename": filename,
            "download_url": f"http://{response.location}/download?filename={filename}"
            # Use the node address from response
        }, status=200)
    else:
        return web.json_response({"error": "File not found"}, status=404)


def request_file_from_node(filename):
    try:
        with grpc.insecure_channel(f"{next_node}") as channel:
            stub = nod_pb2_grpc.NodeServiceStub(channel)
            response = stub.RequestFile(
                nod_pb2.FileRequest(filename=filename, origin_node=f"{local_ip}:{rest_port}"))
        return response
    except grpc.RpcError as e:
        print(f"gRPC error occurred: {e}")
        return nod_pb2.FileResponse(content="", found=False, location="")


async def download_file(request):
    filename = request.query.get('filename')
    if not filename:
        return web.json_response({"error": "Missing 'filename' parameter"}, status=400)

    # Check if the file is local
    file_path = os.path.join(files_directory, filename)
    if os.path.isfile(file_path):
        # Serve the file
        return web.FileResponse(file_path)

    return web.json_response({"error": "File not found"}, status=404)


async def list_files(request):
    response = await asyncio.get_event_loop().run_in_executor(
        None, list_files_from_node
    )

    # Convert the RepeatedScalarContainer to a regular Python list
    files_list = list(response.files)

    return web.json_response({"files": files_list}, status=200)


async def upload_file(request):
    reader = await request.multipart()
    field = await reader.next()

    if not field:
        return web.json_response({"error": "No file uploaded"}, status=400)

    filename = field.filename
    if not filename:
        return web.json_response({"error": "No filename provided"}, status=400)

    file_path = os.path.join(files_directory, filename)

    with open(file_path, 'wb') as f:
        while True:
            chunk = await field.read_chunk()  # 8192 bytes by default.
            if not chunk:
                break
            f.write(chunk)

    return web.json_response({"message": f"File '{filename}' uploaded successfully"}, status=201)


def list_files_from_node():
    try:
        with grpc.insecure_channel(f"{next_node}") as channel:
            stub = nod_pb2_grpc.NodeServiceStub(channel)
            response = stub.ListFiles(nod_pb2.ListFilesRequest(origin_node=f"{local_ip}:{rest_port}"))
        return response
    except grpc.RpcError as e:
        print(f"gRPC error occurred: {e}")
        return nod_pb2.ListFilesResponse(files=[])


def init_rest():
    app = web.Application()
    app.router.add_get('/search', search_file)
    app.router.add_get('/download', download_file)
    app.router.add_get('/list-files', list_files)
    app.router.add_post('/upload', upload_file)  # New endpoint for file upload
    return app


if __name__ == "__main__":
    # Ensure the "files" directory exists
    if not os.path.exists(files_directory):
        os.makedirs(files_directory)

    # Start the gRPC server in a separate thread.
    grpc_thread = Thread(target=serve_grpc, args=(grpc_port, next_node))
    grpc_thread.start()

    # Start the asynchronous REST API.
    print(f"REST API started on port {rest_port}")
    web.run_app(init_rest(), port=int(rest_port))
