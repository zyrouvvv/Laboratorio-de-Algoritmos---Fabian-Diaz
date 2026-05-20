#1. Definir una lista que almacene por asignación los nombres de 5 personas. Contar cuántos de esos nombres tienen 5 o más caracteres y mostrarlo.

lista = ["Fabian", "Virginia", "Luciano", "Camila", "Kevin"]

contador = 0

for x in range(5):
    if len(lista[x]) >= 5:
        contador += 1

print("Cantidad de nombres con 5 o más caracteres:" + contador)
