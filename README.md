
## Información de la materia
ST0263 Tópicos especiales en telemática

## Integrantes del Equipo
- **Daniela Arango Gutierrez**

## Profesor
**Alvaro Enrique Ospina Sanjuan**  aeospinas@eafit.brightspace.com

## Nombre del Proyecto
**# Reto 1:Arquitectura P2P y Comunicación entre procesos mediante API REST, RPC y MOM**

## Descripción de la actividad
El proyecto consiste en la implementación de una red P2P (peer-to-peer) diseñada para permitir la distribución descentralizada de archivos entre nodos. En esta red, cada nodo opera tanto como cliente como servidor, facilitando la solicitud y transferencia de archivos de manera directa entre los participantes de la red. 

## Objetivos Logrados en el Proyecto
- Se creó y desplegó con éxito un sistema distribuido para la gestión de archivos utilizando **gRPC** y **API REST**.
- Se implementó la comunicación entre nodos utilizando **gRPC** y se configuró el servidor **API REST** para la interacción con los usuarios.
- El proyecto fue subido a **AWS** para realizar pruebas en un entorno de nube, facilitando la validación del sistema en condiciones reales.

## Objetivos No Logrados
- Implementar **MOM** (debido a que no se ajustaba a la architectura y funcionalidad del proyecto)

## Instrucciones para Configuración y Creación del Proyecto

## Antes de Comenzar

1. **Crear una Cuenta en AWS**:
   - Si eres nuevo en AWS, [crea una cuenta en AWS](https://aws.amazon.com/) para poder utilizar los servicios en la nube. 

## Configuración de Instancias EC2

1. **Iniciar Sesión en la Consola de AWS**:
   - Ve a la [Consola de administración de AWS](https://aws.amazon.com/console/) e inicia sesión con tu cuenta.

2. **Crear Instancias EC2**:
   - **Acceder al Servicio EC2**:
     En la consola de AWS, busca "EC2" en el menú de servicios y haz clic en "Instancias".

   - **Lanzar Instancias**:
     Haz clic en "Launch Instance" para crear una nueva instancia.

   - **Seleccionar una Imagen de Máquina de Amazon (AMI)**:
     Elige una AMI adecuada, como "Ubuntu Server 20.04 LTS".

   - **Elegir un Tipo de Instancia**:
     Selecciona un tipo de instancia según tus necesidades. Para pruebas, una instancia `t2.micro` (con el nivel gratuito) puede ser suficiente.

   - **Configurar Detalles de la Instancia**:
     - Configura la red y las subredes según tus requisitos. Asegúrate de que todas las instancias estén en la misma red para facilitar la comunicación entre ellas.

   - **Agregar Almacenamiento**:
     Puedes usar el almacenamiento predeterminado o agregar almacenamiento adicional si es necesario.

   - **Configurar el Grupo de Seguridad**:
     Crea un nuevo grupo de seguridad o selecciona uno existente. Asegúrate de permitir el tráfico de entrada en los puertos que tu aplicación necesita ( TCP 50051 para gRPC, TCP 8080 para HTTP).

   - **Revisar y Lanzar**:
     Revisa todas las configuraciones y haz clic en "Launch". Selecciona un par de claves existente o crea uno nuevo para acceder a las instancias.

   - **Repetir el Proceso**:
     Repite los pasos a-g para crear dos instancias adicionales, asegurándote de que todas las instancias estén en la misma red y grupo de seguridad.

3. **Conectar a las Instancias EC2**:
   - Una vez que las instancias estén en funcionamiento, puedes conectarte a ellas utilizando SSH o el método que hayas configurado.

   ##Clonar el Repositorio

En cada instancia EC2, sigue estos pasos para clonar el repositorio:

- **Asegúrate de tener Git instalado**:
   - Para **Ubuntu**, instala Git con:
     ```bash
     sudo apt-get install git
     ```

- **Clona el repositorio**:
   - Usa el siguiente comando para clonar el repositorio:
     ```bash
     git clone https://github.com/daniarango378/daniarango378-st0263.git
     ```

- **Navega al directorio clonado**:
   - Accede al directorio del repositorio clonado con:
     ```bash
     cd daniarango378-st0263
     ```
- **Entra al directorio del proyecto**:
   - Accede al directorio del proyecto::
     ```bash
     cd Tele2
     ```
     - **Entra al nodo en que vas a trabajar**:
   - Accede al directorio del Nodo:
     ```bash
     cd Nodo1 
     ```
 ## Instalar Python y Librerías

 En cada instancia siga los siguientes pasos para instalar python

- **Instalar Python 3**:
   - En **Ubuntu**:
     ```bash
     sudo apt-get update
     sudo apt-get install -y python3 python3-pip
     ```
 - **Instalar pip** (si no está instalado automáticamente):
   - En **Ubuntu**:
     ```bash
     sudo apt-get install -y python3-pip
     ```

- **Instalar las librerías necesarias**:
   - Asegúrate de estar en el directorio del proyecto del nodo.
  
   - Instala las librerías usando pip:
     ```bash
     pip3 install -r requirements.txt
     ```
## Crear Archivos .env

Para cada nodo, sigue estos pasos para crear el archivo `.env` en el directorio del proyecto:

1. **Crea el archivo `.env` en cada instancia**:
   - Ejecuta el siguiente comando:
     ```bash
     nano .env
     ```

2. **Añade el siguiente contenido al archivo `.env`**, ajustando los valores según sea necesario para cada nodo. 
En el nodo1 se pone la ip del Nodo2 en "NEXT_NODE_IP=", en el Nodo2 la del tres y así sucesivamente
En "LOCAL_IP=" se pone la ip del nodo que se tiene abierto

   ```plaintext
   GRPC_PORT=50057
   REST_PORT=8080
   NEXT_NODE_IP=127.0.0.1
   NEXT_NODE_PORT=50057
   LOCAL_IP=127.0.0.1
   ```
3. **Guarda y cierra el archivo** (Ctrl+X, luego Y para confirmar y Enter para guardar).

## Ejecutar el Código

En cada nodo corre lo siguiente para inicializar los nodos:
 ```
 python3 node.py
 ```

## Funcionalidades

1. **Listar Archivos**
   - **Descripción**: Obtiene una lista de todos los archivos disponibles en el nodo actual y en los nodos siguientes en la cadena.
   - **URL**: `http://<LOCAL_IP>:<REST_PORT>/list-files`
   - **Método**: GET
   - **Cómo usar en el navegador**:
     - Abre tu navegador y visita la siguiente URL:
       ```plaintext
       http://127.0.0.1:8080/list-files
       ```
       -Reemplaza "127.0.0.1" por la ip del nodo por el que deseas iniciar la busqueda
   - **Respuesta Esperada**:
     ```json
     {
       "files": ["file1.txt", "file2.jpg"]
     }
     ```

2. **Subir Archivos**
   - **Descripción**: Permite subir un archivo al nodo actual.
   - **URL**: `http://<LOCAL_IP>:<REST_PORT>/upload`
   - **Método**: POST
   - **Tipo de Contenido**: multipart/form-data
   - **Cómo usar en el navegador**:
     - No puedes usar el navegador directamente para enviar archivos mediante multipart/form-data. En su lugar, usa una herramienta como Postman para hacer una solicitud POST con el archivo adjunto.

3. **Buscar Archivos**
   - **Descripción**: Busca un archivo en los nodos de la red. Si el archivo está en el nodo actual, devuelve la URL para la descarga.
   - **URL**: `http://<LOCAL_IP>:<REST_PORT>/search?filename=<FILENAME>`
   - **Método**: GET
   - **Cómo usar en el navegador**:
     - Abre tu navegador y visita la siguiente URL, reemplazando `<FILENAME>` con el nombre del archivo que deseas buscar:
       ```plaintext
       http://127.0.0.1:8080/search?filename=example.txt
       ```
   - **Respuesta Esperada**:
     ```json
     {
       "filename": "example.txt",
       "download_url": "http://127.0.0.1:8080/download?filename=example.txt"
     }
     ```

4. **Descargar Archivos**
   - **Descripción**: Permite descargar un archivo disponible en el nodo actual.
   - **URL**: `http://<LOCAL_IP>:<REST_PORT>/download?filename=<FILENAME>`
   - **Método**: GET
   - **Cómo usar en el navegador**:
     - Abre tu navegador y visita la siguiente URL, reemplazando `<FILENAME>` con el nombre del archivo que deseas descargar:
       ```plaintext
       http://127.0.0.1:8080/download?filename=example.txt
       ```
   - **Respuesta Esperada**: El archivo será descargado si está disponible en el nodo actual.

## Video

## Documentación de actividades

Las actividades planteadas en el enunciado del reto estan en la wiki.




