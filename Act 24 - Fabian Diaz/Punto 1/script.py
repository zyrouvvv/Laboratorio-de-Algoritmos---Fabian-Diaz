"""1-
Una ciudad inteligente cuenta con sensores que miden las partículas contaminantes de
dióxido de carbono (CO2) en diferentes puntos geográficos.
 Crear un diccionario donde la Clave sea el nombre del barrio o estación de
monitoreo (ej: &quot;San Telmo&quot;) y el Valor sea una lista de flotantes que represente
las últimas 3 lecturas de contaminación tomadas en el día.
Desarrollar las siguientes funciones:
1. Cargar sensores: Ingresar por teclado 3 estaciones de monitoreo y, para cada
una, solicitar las 3 lecturas consecutivas de CO2 (en partes por millón - ppm).
2. Reportar promedios: Calcular y mostrar el promedio de contaminación de cada
barrio.
3. Alerta ambiental: Mostrar en pantalla una alerta roja de &quot;Protocolo de
Emergencia&quot; únicamente para las estaciones cuyo promedio de contaminación
supere las 400 ppm."""

sensores = {}

def cargar_sensores():
    for i in range(3):
        estacion = input("Ingrese el nombre de la estación: ")
        lecturas = []
        for j in range(3):
            lectura = float(input("Ingrese la lectura de CO2 (ppm): "))
            lecturas.append(lectura)

        sensores[estacion] = lecturas


def reportar_promedios():
    print("Promedios de contaminacion")

    for estacion, lecturas in sensores.items():
        promedio = sum(lecturas) / 3

        print(estacion, ":", promedio, "ppm")


def alerta_ambiental():
    print("Alertas ambientales")

    for estacion, lecturas in sensores.items():
        promedio = sum(lecturas) / 3

        if promedio > 400:
            print("Estación:", estacion)
            print("Promedio:", promedio, "ppm")


cargar_sensores()
reportar_promedios()
alerta_ambiental()
