# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import nod_pb2 as nod__pb2

GRPC_GENERATED_VERSION = '1.66.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in nod_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class NodeServiceStub(object):
    """The gRPC service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RequestFile = channel.unary_unary(
                '/nod.NodeService/RequestFile',
                request_serializer=nod__pb2.FileRequest.SerializeToString,
                response_deserializer=nod__pb2.FileResponse.FromString,
                _registered_method=True)
        self.ListFiles = channel.unary_unary(
                '/nod.NodeService/ListFiles',
                request_serializer=nod__pb2.ListFilesRequest.SerializeToString,
                response_deserializer=nod__pb2.ListFilesResponse.FromString,
                _registered_method=True)


class NodeServiceServicer(object):
    """The gRPC service definition.
    """

    def RequestFile(self, request, context):
        """Request a file from the node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Request the list of all files from the node.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_NodeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RequestFile': grpc.unary_unary_rpc_method_handler(
                    servicer.RequestFile,
                    request_deserializer=nod__pb2.FileRequest.FromString,
                    response_serializer=nod__pb2.FileResponse.SerializeToString,
            ),
            'ListFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.ListFiles,
                    request_deserializer=nod__pb2.ListFilesRequest.FromString,
                    response_serializer=nod__pb2.ListFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'nod.NodeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('nod.NodeService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class NodeService(object):
    """The gRPC service definition.
    """

    @staticmethod
    def RequestFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nod.NodeService/RequestFile',
            nod__pb2.FileRequest.SerializeToString,
            nod__pb2.FileResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def ListFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/nod.NodeService/ListFiles',
            nod__pb2.ListFilesRequest.SerializeToString,
            nod__pb2.ListFilesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
