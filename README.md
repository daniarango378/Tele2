Información de la materia
ST0263 Tópicos especiales en telemática
ST0263 Tópicos especiales en telemática
Integrantes del Equipo
Jorge A. Villarreal
Daniel Gonzalez Bernal
Martin Villegas
Profesor
Edwin Nelson Montoya Munera, emontoya@eafit.edu.co
Nombre del Proyecto
Reto 4 Tópicos Especiales en Telemática

Objetivos Logrados en el Proyecto
Se creó y desplegó con éxito un sistema distribuido para la gestión de archivos utilizando gRPC y REST.
Se implementó la comunicación entre nodos utilizando gRPC y se configuró el servidor REST para la interacción con los usuarios.
Se subió el proyecto a AWS para realizar pruebas en un entorno de nube, facilitando la validación del sistema en condiciones reales.
Objetivos No Logrados
Todo el proyecto se logró según los objetivos establecidos.
Instrucciones para Configuración y Creación del Proyecto
Antes de Comenzar
Crear una Cuenta en AWS: Si eres nuevo en AWS, crea una cuenta para poder utilizar los servicios de la nube. Puedes obtener un crédito gratuito inicial para probar los servicios.

Configurar AWS CLI: Asegúrate de tener AWS CLI configurado en tu entorno.

bash
Copiar código
aws configure
Configuración del Entorno Local
Clonar el Repositorio:

bash
Copiar código
git clone https://github.com/tu-usuario/proyecto-distribucion-archivos.git
cd proyecto-distribucion-archivos
Instalar las Dependencias:

bash
Copiar código
pip install -r requirements.txt
Configurar las Variables de Entorno:

Crea un archivo .env en la raíz del proyecto y define las variables necesarias. Un ejemplo de archivo .env podría verse así:

env
Copiar código
GRPC_SERVER_PORT=50051
REST_SERVER_PORT=8080
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
Despliegue en AWS
Configurar AWS CLI:

Asegúrate de que tienes configuradas las credenciales de AWS en tu entorno.

bash
Copiar código
aws configure
Crear y Configurar Recursos en AWS:

Crear una Instancia EC2 para el Servidor:

Utiliza la consola de AWS o CLI para crear una instancia EC2 y configurar la red y el almacenamiento necesarios.

Desplegar el Proyecto:

Sigue las instrucciones específicas para desplegar el código en la instancia EC2.

Probar el Proyecto en AWS:

Realiza pruebas para asegurarte de que el sistema funciona correctamente en el entorno de nube.

Estructura del Proyecto
grpc_server.py: Implementación del servidor gRPC para la comunicación entre nodos.
rest_server.py: Implementación del servidor REST para la interacción con usuarios y otros sistemas.
.env: Archivo de configuración con las variables de entorno necesarias.
nod.proto: Archivo de definiciones para gRPC, utilizado para generar nod_pb2.py y nod_pb2_grpc.py.
Dependencias del Proyecto
Este proyecto utiliza varias librerías para manejar diferentes aspectos de la funcionalidad:

asyncio
Descripción: Facilita la programación asíncrona, permitiendo la ejecución de corutinas y tareas de forma no bloqueante.
Uso: Maneja operaciones de I/O como solicitudes de red de manera eficiente.
aiohttp (submódulo web)
Descripción: Permite manejar solicitudes HTTP de forma asíncrona y construir servidores web.
Uso: Implementación del servidor REST para exponer las APIs del proyecto.
threading (submódulo Thread)
Descripción: Proporciona la clase Thread para la ejecución concurrente de código mediante hilos.
Uso: Ejecuta el servidor gRPC en paralelo con el servidor REST.
concurrent.futures
Descripción: Proporciona una interfaz para ejecutar tareas de forma asíncrona usando un pool de hilos o procesos.
Uso: Maneja operaciones concurrentes para mejorar el rendimiento del sistema.
grpc
Descripción: Implementa servicios de comunicación remota utilizando RPC de alto rendimiento.
Uso: Implementación del servidor y cliente gRPC para la transferencia de archivos entre nodos.
nod_pb2 y nod_pb2_grpc
Descripción: Archivos generados por protoc que definen los mensajes y servicios gRPC.
Uso: Implementación de los mensajes y servicios definidos en nod.proto.
os
Descripción: Permite interactuar con el sistema operativo.
Uso: Manipulación de rutas de archivos y gestión de variables de entorno.
dotenv (submódulo load_dotenv)
Descripción: Facilita la carga de variables de entorno desde un archivo .env.
Uso: Carga de configuraciones clave sin tener que hardcodearlas en el código fuente.
Contribuciones
Las contribuciones son bienvenidas. Por favor, sigue las buenas prácticas de desarrollo y documenta adecuadamente cualquier cambio.
