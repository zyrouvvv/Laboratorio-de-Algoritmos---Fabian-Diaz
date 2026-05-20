#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

mayor7 = 0
menor = 0

for x in range(10):
    valor = int(input("Ingrese un numero: "))

    if valor >= 7:
        mayor7 = mayor7 + 1
    else:
        menor = menor + 1

print(f"La cantidad de valores mayores o iguales a 7 es: {mayor7}")
print(f"La cantidad de valores menores a 7 es: {menor}")