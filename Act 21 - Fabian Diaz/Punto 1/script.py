"""1-
Confeccionar un programa con las siguientes funciones:
1)Cargar una lista de 5 enteros.
2)Retornar el mayor y menor valor de la lista mediante una tupla.
Desempaquetar la tupla en el bloque principal y mostrar el mayor y menor."""




def cargar():
    lista = []
    for x in range (5):
        valor = int(input(f"Ingrese el valor de la posicion {x+1}: "))
        lista.append(valor)
    return lista 

def mayorYmenor(lista):
    mayor = lista[0]
    menor = lista[0]

    for valor in lista:
        if valor > mayor:
            mayor = valor
        elif valor < menor:
            menor = valor
    return (menor, mayor)

lista = cargar()
resultado = mayorYmenor(lista)
menor, mayor = resultado

print("Menor:", menor)
print("Mayor:", mayor)
    



