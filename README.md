# Transferencia de Imágenes entre Sistemas Odoo

Este proyecto contiene un script en Python que transfiere imágenes de productos de un sistema Odoo a otro utilizando la API XML-RPC. El script lee los datos de productos de un sistema Odoo y actualiza los productos correspondientes en otro sistema Odoo con las imágenes obtenidas.

## Requisitos

- Python 3.6 o superior
- [python-dotenv](https://pypi.org/project/python-dotenv/) para cargar variables de entorno desde un archivo `.env`

## Instalación

1. **Clona el repositorio**

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
   
2. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   
## Configuración

1. **Crea un archivo .env**

   ```bash
   SOURCE_URL=https://tu_sistema_odoo.com
   SOURCE_DB=tu_base_de_datos_origen
   SOURCE_USERNAME=tu_usuario_origen
   SOURCE_PASSWORD=tu_contraseña_origen

   DESTINATION_URL=https://tu_otro_sistema_odoo.com
   DESTINATION_DB=tu_base_de_datos_destino
   DESTINATION_USERNAME=tu_usuario_destino
   DESTINATION_PASSWORD=tu_contraseña_destino

2. **Reemplaza los valores con la información correspondiente de tus sistemas Odoo:**

   ```bash
   SOURCE_URL: La URL del sistema Odoo de origen.
   SOURCE_DB: El nombre de la base de datos del sistema Odoo de origen.
   SOURCE_USERNAME: El nombre de usuario para el sistema Odoo de origen.
   SOURCE_PASSWORD: La contraseña para el sistema Odoo de origen.
   DESTINATION_URL: La URL del sistema Odoo de destino.
   DESTINATION_DB: El nombre de la base de datos del sistema Odoo de destino.
   DESTINATION_USERNAME: El nombre de usuario para el sistema Odoo de destino.
   DESTINATION_PASSWORD: La contraseña para el sistema Odoo de destino.

3. **Verifica el archivo .env**

   ```bash
   Asegúrate de que el archivo .env esté en el mismo directorio que el script y 
   que tenga los permisos correctos para ser leído por el script.
   
## Ejecución

1. **Para ejecutar el script, usa el siguiente comando en tu terminal (Ubicado en el mismo directorio del script):**

   ```bash
   python main.py
