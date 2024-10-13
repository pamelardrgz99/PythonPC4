import requests
import zipfile

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    with open(nombre_archivo, 'wb') as file:
            file.write(response.content)

def crear_zip(nombre_archivo, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        zipf.write(nombre_archivo)
    print(f"Imagen comprimida en el archivo {nombre_zip}")


def descomprimir_zip(nombre_zip, directorio_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as zipf:
        zipf.extractall(directorio_destino)
    print(f"Archivo {nombre_zip} descomprimido en {directorio_destino}")

def main():
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"
    nombre_zip = "imagen_comprimida.zip"
    directorio_destino = "."

# Descargar la imagen
    descargar_imagen(url, nombre_imagen)

# Crear un archivo zip con la imagen
    crear_zip(nombre_imagen, nombre_zip)

# Descomprimir el archivo zip
    descomprimir_zip(nombre_zip, directorio_destino)

if __name__ == "__main__":
    main()




