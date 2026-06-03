"""1. Desarrollar un programa que solicite la carga de tres valores y muestre el
menor. Desde el bloque principal del programa llamar 2 veces a dicha
función (sin utilizar una estructura repetitiva)"""

def mostrarMenor(valor1, valor2, valor3):
    if valor1 < valor2 and valor1 < valor3:
        print(f"El menor numero es: {valor1}")
    else: 
        if valor2 < valor3:
            print(f"El menor numero es: {valor2}")
        else:
            print(f"El menor numero es: {valor3}")


def cargar():
    valor1 = int(input("Ingrese el primer valor: "))
    valor2 = int(input("Ingrese el primer valor: "))
    valor3 = int(input("Ingrese el primer valor: "))
    mostrarMenor(valor1, valor2, valor3)

cargar()    