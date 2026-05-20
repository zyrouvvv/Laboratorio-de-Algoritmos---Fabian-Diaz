""""1. Se desea desarrollar un programa que permita registrar los nombres y las
calificaciones de 6 estudiantes. Luego de cargar los datos, se debe mostrar el
nombre del estudiante con la nota más alta, junto con su nota. Al igual que el
estudiante con la nota más baja. Informar si hay estudiantes con la misma nota
máxima o mínima. """

nombres = []
notas = []

for x in range(6):
    nombre = input(f"Ingrese el nombre del estudiante {x+1}: ")
    nota = float(input(f"Ingrese la nota de {nombre}: "))

    nombres.append(nombre)
    notas.append(nota)

maxNota = notas[0]
minNota = notas[0]

for x in range(6):

    if notas[x] > maxNota:
        maxNota = notas[x]

    if notas[x] < minNota:
        minNota = notas[x]

print("Estudiante con nota más alta:")
for x in range(6):
    if notas[x] == maxNota:
        print(nombres[x], notas[x])

print("Estudiante con nota más baja:")
for x in range(6):
    if notas[x] == minNota:
        print(nombres[x], notas[x])