#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.


suma = 0

for x in range(1,5):
    altura = int(input(f"Ingrese la altura de la persona {x}: "))

    suma = suma + altura
    promedio = suma / 4

print(f"El promedio de las alturas es: {promedio}")