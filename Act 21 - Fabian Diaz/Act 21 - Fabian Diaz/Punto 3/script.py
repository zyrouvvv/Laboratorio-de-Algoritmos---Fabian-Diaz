"""Almacenar en una lista 5 empleados, cada elemento de la lista es una sub lista
con el nombre del empleado junto a sus últimos tres sueldos (estos tres valores en
una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a
10000 en los últimos tres meses.
Tener en cuenta que la estructura de datos si se carga por asignación debería ser
similar a:
empleados = [[&quot;juan&quot;,(2000,3000,4233)] , [&quot;ana&quot;,(3444,1000,5333)] , etc. ]"""

def carga():
    empleados = []
    
    for x in range(5):
        nombre = input(f"Ingrese el nombre del empleado {x+1}: ")

        sueldo1 = int(input("Ingrese el sueldo 1: "))
        sueldo2 = int(input("Ingrese el sueldo 2: "))
        sueldo3 = int(input("Ingrese el sueldo 3: "))

        empleados.append([nombre, (sueldo1,sueldo2,sueldo3)])

        return empleados
    
def totalCobrado(empleados):

    for empleado in empleados:
        total = 0
    
        for sueldo in empleado[1]:
            total = total + sueldo
        print(empleado[0], "cobro", total)

def ingresoMayor(empleados):
    print("Empleados con mas de 10000: ")

    for empleado in empleados:
        total = 0
        for sueldo in empleado[1]:
            total = total + sueldo
        if total > 10000:
            print(empleado[0])


empleados = carga()
totalCobrado(empleados)
ingresoMayor(empleados)