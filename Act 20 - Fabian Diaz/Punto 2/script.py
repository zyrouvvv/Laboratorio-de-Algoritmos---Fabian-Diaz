"""2. Desarrollar una aplicación que permita ingresar por teclado los nombres de
5 artículos y sus precios.
Definir las siguientes funciones:
1) Cargar los nombres de artículos y sus precios.
2) Imprimir los nombres y precios.
3) Imprimir el nombre de artículo con un precio mayor
4) Ingresar por teclado un importe y luego mostrar todos los artículos con
un precio menor igual al valor ingresado."""


def ArticulosYPrecios():
    for x in range(5):
        articulo = input(f"Ingrese el articulo {x+1}: ")
        precio = int(input(f"Ingrese el precio del articulo {x+1}: "))
        articulos.append(articulo)
        precios.append(precio)

def Imprimir():
    for x in range(len(articulos)):
        print(articulos[x], precios[x])

def mayorPrecio():
    mayor = precios[0]

    for x in range(1, len(precios)):
        if precios[x] > mayor:
            mayor = precios[x]

    print(f"El artículo con mayor precio cuesta {mayor}")

def importes():
    importe = int(input("Ingrese un importe para comparar: "))

    print("Artículos con precio menor o igual al importe:")
    for x in range(len(precios)):
        if precios[x] <= importe:
            print(articulos[x], precios[x])

articulos = []
precios = []

ArticulosYPrecios()
Imprimir()
mayorPrecio()
importes()