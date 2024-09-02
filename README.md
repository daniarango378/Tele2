
## Información de la materia
ST0263 Tópicos especiales en telemática

## Integrantes del Equipo
- **Daniela Arango Gutierrez**

## Profesor
**Alvaro Enrique Ospina Sanjuan**  

## Nombre del Proyecto
**# Reto 1:Arquitectura P2P y Comunicación entre procesos mediante API REST, RPC y MOM**

## Objetivos Logrados en el Proyecto
- Se creó y desplegó con éxito un sistema distribuido para la gestión de archivos utilizando **gRPC** y **API REST**.
- Se implementó la comunicación entre nodos utilizando **gRPC** y se configuró el servidor **API REST** para la interacción con los usuarios.
- El proyecto fue subido a **AWS** para realizar pruebas en un entorno de nube, facilitando la validación del sistema en condiciones reales.

## Objetivos No Logrados
- Implementar **MOM**

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

4. **Clonar el Repositorio**

En cada instancia EC2, sigue estos pasos para clonar el repositorio:

- **Asegúrate de tener Git instalado**:
   - Para **Ubuntu**, instala Git con:
     ```bash
     sudo apt-get install git
     ```

- **Clona el repositorio**:
   - Usa el siguiente comando para clonar el repositorio:
     ```bash
     git clone ...
     ```

- **Navega al directorio clonado**:
   - Accede al directorio del repositorio clonado con:
     ```bash
     cd Tele2
     ```
- **Entra al directorio del proyecto**:
   - Accede al directorio del repositorio clonado con:
     ```bash
     cd Tele2
     ```
     - **Entra al nodo en que vas a trabajar**:
   - Accede al directorio del repositorio clonado con:
     ```bash
     cd Nodo1 
     ```




