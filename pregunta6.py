def contar_lineas_codigo(ruta_archivo):
    # Validar si el archivo tiene extension .py
    if not ruta_archivo.endswith('.py'):
        print("El archivo debe tener extensión .py")
        return

    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas = archivo.readlines()
            
        lineas_codigo = 0
        for linea in lineas:
            # Eliminar espacios en blanco al inicio y final de la linea
            linea = linea.strip()
            # Contar lineas que no sean comentarios o lineas vacias
            if linea and not linea.startswith('#'):
                lineas_codigo += 1

        print(f"El archivo tiene {lineas_codigo} lineas de codigo.")
    except FileNotFoundError:
        print("Error, archivo no encontrado.")

if __name__ == "__main__":
    ruta = input("Ingrese la ruta del archivo .py: ")
    contar_lineas_codigo(ruta)
