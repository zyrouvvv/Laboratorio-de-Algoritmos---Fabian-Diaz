"""3-
Un sistema de hogar inteligente monitorea qué electrodomésticos consumen más energía
en cada habitación de la casa.
 Crear un diccionario donde la Clave sea el nombre del ambiente (ej: &quot;Cocina&quot;,
&quot;Dormitorio&quot;) y el Valor sea una lista de tuplas, donde cada tupla represente un
dispositivo activo y su consumo: [(nombre_dispositivo, consumo_watts)].
Desarrollar las siguientes funciones:
1. Cargar dispositivos: Solicitar la carga de 3 habitaciones. Para cada habitación,
ingresar el nombre de los dispositivos activos y su consumo en Watts hasta que el
operador decida no cargar más para ese ambiente.
2. Consumo por habitación: Imprimir el listado de habitaciones y el consumo total
en Watts acumulado en cada una de ellas.
3. Dispositivo crítico: Buscar e informar el nombre del electrodoméstico que más
energía consume de toda la casa (el valor máximo individual dentro de todas las
listas del diccionario), indicando en qué habitación se encuentra."""


def cargar():
    habitaciones = {}

    for i in range(3):
        habitacion = input(f"Ingrese el nombre de la habitación {i+1}: ")
        dispositivos = []

        while True:
            dispositivo = input("Ingrese el dispositivo activo: ")
            consumo = int(input("Ingrese su consumo en Watts: "))

            dispositivos.append((dispositivo, consumo))

            continuar = input("¿Desea cargar otro dispositivo? (s/n): ")
            if continuar.lower() == "n":
                break

        habitaciones[habitacion] = dispositivos

    return habitaciones

def consumo(habitaciones):
    print("Listado de habitaciones:")

    for habitacion, dispositivos in habitaciones.items():
        total = 0

        for dispositivo, watts in dispositivos:
            total += watts

        print(f"Habitación: {habitacion} - Consumo: {total} Watts")

def dispositivo_critico(habitaciones):
    print("Dispositivo que mas consume: ")

    mayor_consumo = 0
    nombre_mayor = ""
    habitacion_mayor = ""

    for habitacion, dispositivos in habitaciones.items():
        for dispositivo, watts in dispositivos:
            if watts > mayor_consumo:
                mayor_consumo = watts
                nombre_mayor = dispositivo
                habitacion_mayor = habitacion

    print(f"Dispositivo que más consume: {nombre_mayor}")
    print(f"Habitación: {habitacion_mayor}")
    print(f"Consumo: {mayor_consumo} Watts")
    
habitaciones = cargar()
consumo(habitaciones)
dispositivo_critico(habitaciones)
