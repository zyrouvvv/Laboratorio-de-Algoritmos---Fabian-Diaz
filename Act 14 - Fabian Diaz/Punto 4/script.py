#4. Cargar por teclado y almacenar en una lista las alturas de 5 personas (valores float) Obtener el promedio de las mismas. Contar cuántas personas son más altas que el promedio y cuántas más bajas.

alturas = []

for x in range(5):
    valor = float(input(f"Ingrese la altura de la persona {x+1}: "))
    alturas.append(valor)

suma = 0

for x in range (5):
    suma += alturas[x]

promedio = suma / 5

masAltas = 0
masBajas = 0

for x in range(5):
    if alturas[x] > promedio:
        masAltas += 1
    elif alturas[x] < promedio:
        masBajas += 1

print(f"El promedio de todas las alturas es: {promedio}")
print(f"La cantidad de personas mas altas que el promedio es: {masAltas}")
print(f"La cantidad de personas mas bajas que el promedio es: {masBajas}")


