import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    
    # Solicitar al usuario el nombre de una fuente
    fuente_usuario = input("Ingrese el nombre de una fuente")
    
    # Obtener la lista de fuentes disponibles
    fuentes_disponibles = figlet.getFonts()
    
    # Seleccionar una fuente aleatoria si no se ingresó ninguna
    if not fuente_usuario:
        fuente_seleccionada = random.choice(fuentes_disponibles)
    else:
        if fuente_usuario in fuentes_disponibles:
            fuente_seleccionada = fuente_usuario
        else:
            print("Fuente no disponible, se seleccionará una fuente aleatoria.")
            fuente_seleccionada = random.choice(fuentes_disponibles)
    
    # Establecer la fuente seleccionada
    figlet.setFont(font=fuente_seleccionada)
    
    # Solicitar al usuario un texto
    texto_imprimir = input("Ingrese el texto a imprimir: ")
    
    # Imprimir el texto usando la fuente apropiada
    print(figlet.renderText(texto_imprimir))

if __name__ == "__main__":
    main()
    
