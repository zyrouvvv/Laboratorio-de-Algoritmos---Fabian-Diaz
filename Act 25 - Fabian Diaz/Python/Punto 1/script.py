"""1-
Confeccionar un programa que permita registrar las temperaturas máximas de las últimas
6 horas en una lista.
Desarrollar las siguientes funciones:
1. Carga: Solicitar al operador el ingreso por teclado de las 6 temperaturas y
almacenarlas en una lista.
2. Procesar Extremos: Recibir la lista como parámetro y retornar una tupla que
contenga en su primer componente el valor máximo y en el segundo el valor
mínimo.
3. Bloque Principal: Desempaquetar la tupla devuelta por la función anterior en dos
variables individuales (máxima y mínima) y mostrarlas en pantalla con un mensaje
descriptivo."""


def cargar():
    temperaturas = []
    for i in range(6):
        temperatura = int(input(f"Ingrese la temperatura {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

def extremos(temperaturas):
    maximo = temperaturas[0]
    minimo = temperaturas[1]

    for temperatura in temperaturas:
        if maximo < temperatura:
            maximo = temperatura
        elif minimo > temperatura:
            minimo = temperatura
    return maximo, minimo

temperaturas = cargar()
maximo, minimo = extremos(temperaturas)
print(f"La temperatura maxima es: {maximo}")
print(f"La temperatura minimo es: {minimo}")



