"""4-
Una empresa de e-commerce utiliza drones autónomos para realizar entregas a domicilio
y necesita rastrear las coordenadas geográficas de sus rutas de vuelo.
 Diseñar un diccionario donde la Clave sea el identificador único del dron (ej:
&quot;DRON-01&quot;) y el Valor sea una lista de tuplas que almacene las coordenadas de
las paradas programadas: [(latitud, longitud)].
Desarrollar las siguientes funciones:
1. Cargar planes de vuelo: Ingresar la información de 3 drones. Solicitar para cada
uno la cantidad de paradas que va a realizar y cargar sus respectivas coordenadas
geográficas.
2. Imprimir rutas: Mostrar el listado completo de los drones junto con sus paradas
de coordenadas asociadas.
3. Ruta más larga: Determinar y mostrar el identificador del dron que tiene la mayor
cantidad de paradas registradas en su ruta de vuelo (la lista con mayor cantidad
de elementos)."""


def cargar():
    drones = {}

    for i in range(3):
        identificador = input(f"Ingrese el identificador del dron {i+1}: ")
        paradas = []

        cantidad = int(input("Ingrese la cantidad de paradas: "))

        for j in range(cantidad):
            latitud = float(input("Ingrese la latitud: "))
            longitud = float(input("Ingrese la longitud: "))

            paradas.append((latitud, longitud))

        drones[identificador] = paradas

    return drones


def imprimir_rutas(drones):
    print("Listado de rutas:")

    for dron, paradas in drones.items():
        print(f"Dron: {dron}")

        for latitud, longitud in paradas:
            print(f"  Latitud: {latitud} - Longitud: {longitud}")


def ruta_mas_larga(drones):
    mayor_cantidad = 0
    dron_mayor = ""

    for dron, paradas in drones.items():
        if len(paradas) > mayor_cantidad:
            mayor_cantidad = len(paradas)
            dron_mayor = dron

    print(f"El dron con la ruta más larga es: {dron_mayor}")
    print(f"Cantidad de paradas: {mayor_cantidad}")


drones = cargar()
imprimir_rutas(drones)
ruta_mas_larga(drones)