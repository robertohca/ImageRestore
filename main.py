import xmlrpc.client
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Configuración del primer sistema Odoo (de donde se extraen las imágenes)
source_url = os.getenv('SOURCE_URL')
source_db = os.getenv('SOURCE_DB')
source_username = os.getenv('SOURCE_USERNAME')
source_password = os.getenv('SOURCE_PASSWORD')

# Conexión al primer sistema Odoo
print("Conectando al sistema Odoo origen...")
source_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(source_url))
source_uid = source_common.authenticate(source_db, source_username, source_password, {})
source_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(source_url))

# Configuración del segundo sistema Odoo (donde se actualizan las imágenes)
destination_url = os.getenv('DESTINATION_URL')
destination_db = os.getenv('DESTINATION_DB')
destination_username = os.getenv('DESTINATION_USERNAME')
destination_password = os.getenv('DESTINATION_PASSWORD')

# Conexión al segundo sistema Odoo
print("Conectando al sistema Odoo destino...")
destination_common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(destination_url))
destination_uid = destination_common.authenticate(destination_db, destination_username, destination_password, {})
destination_models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(destination_url))


# Función para paginar la consulta
def fetch_products(models, db, uid, password, offset=0, limit=100):
    return models.execute_kw(db, uid, password,
                             'product.template', 'search_read',
                             [[], ['id', 'image_1920']], {'offset': offset, 'limit': limit})


print("Iniciando la transferencia de imágenes...")
offset = 0
limit = 100
total_products = 0
while True:
    products = fetch_products(source_models, source_db, source_uid, source_password, offset, limit)
    if not products:
        break

    total_products += len(products)
    print(f"Procesando productos del {offset + 1} al {offset + len(products)}...")

    # Actualizar productos en el segundo sistema Odoo
    for product in products:
        product_id = product['id']
        image = product['image_1920']

        # No convertimos la imagen a Base64, ya que debería estar en formato binario
        # Actualiza el producto en el segundo sistema Odoo
        try:
            destination_models.execute_kw(destination_db, destination_uid, destination_password,
                                          'product.template', 'write',
                                          [[product_id], {'image_1920': image}])
            print(f"Producto {product_id} actualizado correctamente.")
        except Exception as e:
            print(f"Error actualizando producto {product_id}: {e}")

    offset += limit

print(f"Transferencia de imágenes completada. Total de productos procesados: {total_products}.")
