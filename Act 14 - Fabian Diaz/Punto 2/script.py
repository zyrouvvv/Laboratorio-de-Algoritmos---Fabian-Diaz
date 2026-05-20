#2. Una empresa tiene dos turnos (mañana y tarde) en los que trabajan 8 empleados (4 por la mañana y 4 por la tarde) Confeccionar un programa que permita almacenar los sueldos de los empleados agrupados en dos listas. Imprimir las dos listas de sueldos.

mañana = []
tarde = []

for x in range(4):
    nombreM = input(f"Ingrese el sueldo del trabajador de la mañana " + {x+1} + ": ")
    mañana.append(nombreM)

    nombreT = input(f"Ingrese el sueldo del trabajador de la tarde " + {x+1} + ": ")
    tarde.append(nombreT)

print("Turno mañana:")
print(mañana)

print("Turno tarde:")
print(tarde)