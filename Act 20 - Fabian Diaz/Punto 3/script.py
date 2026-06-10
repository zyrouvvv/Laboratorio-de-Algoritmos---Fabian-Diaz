"""3. Confeccionar un programa que permita:
1) Cargar una lista de 10 elementos enteros.
2) Generar dos listas a partir de la primera. En una guardar los valores
positivos y en otra los negativos.
3) Imprimir las dos listas generadas."""

lista1 = []
lista2 = []
lista3 = []

def carga():
    for x in range(10):
        lista = int(input(f"Ingrese el valor numero {x+1}: "))
        lista1.append(lista)
    
def valoresNegativos():
    for x in range(10):
        if lista1[x] < 0:
            lista2.append(lista1[x])

def valoresPositivos():
    for x in range(10):
        if lista1[x] > 0:
            lista3.append(lista1[x])

def imprimir():
    print(f"Lista negativa: {lista2}")
    print(f"Lista positiva: {lista3}")

carga()
valoresNegativos()
valoresPositivos()
imprimir()

