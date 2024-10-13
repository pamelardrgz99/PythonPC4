
def guardar_tabla(n):
    with open(f'tabla-{n}.txt', 'w') as file:
        for i in range(1, 11):
            file.write(f'{n} x {i} = {n * i}\n')

def mostrar_tabla(n):
    try:
        with open(f'tabla-{n}.txt', 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f' Fichero no existe.')

def mostrar_linea_tabla(n, m):
    try:
        with open(f'tabla-{n}.txt', 'r') as file:
            lineas = file.readlines()
            if 1 <= m <= 10:
                print(lineas[m - 1].strip())
            else:
                print('Numero de línea fuera de rango.')
    except FileNotFoundError:
        print(f'Fichero no existe.')

def menu():
    while True:
        print("\nMenu:")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar linea especifica de la tabla de multiplicar")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            n = int(input("Ingrese un numero entre 1 y 10: "))
            if 1 <= n <= 10:
                guardar_tabla(n)
            else:
                print("Numero fuera del rango")
        elif opcion == 2:
            n = int(input("Ingrese un numero entre 1 y 10: "))
            if 1 <= n <= 10:
                mostrar_tabla(n)
            else:
                print("Numero fuera de rango.")
        elif opcion == 3:
            n = int(input("Ingrese un numero entre 1 y 10: "))
            m = int(input("Ingrese la linea que desea ver entre 1 y 10: "))
            if 1 <= n <= 10 and 1 <= m <= 10:
                mostrar_linea_tabla(n, m)
            else:
                print("Numero fuera de rango.")
        elif opcion == 4:
            break
        else:
            print("Error")

if __name__ == "__main__":
    menu()
