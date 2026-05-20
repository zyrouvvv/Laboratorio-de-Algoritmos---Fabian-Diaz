"""1. En un curso de 4 alumnos se registraron las notas de sus exámenes y se
deben procesar de acuerdo a lo siguiente:
a. Ingresar nombre y nota de cada alumno (almacenar los datos en
dos listas paralelas)
b. Realizar un listado que muestre los nombres, notas y condición del
alumno. En la condición, colocar &quot;Muy Bueno&quot; si la nota es mayor o
igual a 8, &quot;Bueno&quot; si la nota está entre 4 y 7, y colocar &quot;Insuficiente&quot;
si la nota es inferior a 4.
c. Imprimir cuántos alumnos tienen la leyenda “Muy Bueno”."""

nombre = []
nota = []

for x in range(4):
    nombreA = input(f"Ingrese el nombre del alumno {x+1}: ")
    nombre.append(nombreA)

    notaA = int(input(f"Ingrese la nota del alumno {x+1}: "))
    nota.append(notaA)

muyBueno = 0

for x in range(4):

    if nota[x] >= 8:
        condicion = "Muy Bueno"
        muyBueno += 1

    elif nota[x] >= 4:
        condicion = "Bueno"

    else:
        condicion = "Insuficiente"

    print(f"Nombre: {nombre[x]} Nota: {nota[x]} Condicion: {condicion}")

print(f"Cantidad de personas con condicion Muy Bueno: {muyBueno}")