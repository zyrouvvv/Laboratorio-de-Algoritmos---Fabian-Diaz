#7. Escribir un programa en el cual: dada una lista de tres valores numéricos distintos se calcule e informe su rango de variación (debe mostrar el mayor y el menor de ellos).

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor (distinto al primer valor): "))
num3 = int(input("Ingrese el primer valor (distinto al segundo y primer valor): "))

mayor = num1
menor = num1

if num2 > mayor:
    mayor = num2
if num3 > mayor:
    mayor = num3


if num2 < menor:
    menor = num2
if num3 < menor:
    menor = num3

print(f"El valor mayor es: {mayor}")
print(f"El valor menor es: {menor}")