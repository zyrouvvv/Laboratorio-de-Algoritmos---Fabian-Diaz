"""2. En una empresa se almacenaron los sueldos de 10 personas.
Desarrollar las siguientes funciones y llamarlas desde el bloque principal:
1) Carga de los sueldos en una lista.
2) Impresión de todos los sueldos.
3) Cuántos tienen un sueldo superior a $4000.
4) Retornar el promedio de los sueldos.
5) Mostrar todos los sueldos que están por debajo del promedio."""


def cargarSueldos():
    sueldos = []
    for i in range(10):
        sueldo = int(input(f"Ingrese el sueldo de la persona {i + 1}: "))
        sueldos.append(sueldo)
    return sueldos


def imprimirSueldos(sueldos):
    print("Lista de sueldos:")
    for sueldo in sueldos:
        print(sueldo)

def contarMayores4000(sueldos):
    contador = 0
    for sueldo in sueldos:
        if sueldo > 4000:
            contador += 1
    return contador



def calcularPromedio(sueldos):
    return sum(sueldos) / len(sueldos)


def mostrarMenoresPromedio(sueldos, promedio):
    print("Sueldos por debajo del promedio:")
    for sueldo in sueldos:
        if sueldo < promedio:
            print(sueldo)

#Programa principal
sueldos = cargarSueldos()

imprimirSueldos(sueldos)

cantidad = contarMayores4000(sueldos)
print(f"Cantidad de personas con sueldo superior a $4000: {cantidad}")

promedio = calcularPromedio(sueldos)
print(f"Promedio de sueldos: {promedio}")

mostrarMenoresPromedio(sueldos, promedio)