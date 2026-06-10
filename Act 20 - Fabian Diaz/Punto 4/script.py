"""4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)"""

edades = []

def cargar():
    for x in range(3):
        edad = int(input(f"Ingrese la edad numero {x+1}: "))
        edades.append(edad)
    
def comparar():
    mayores = 0
    for x in range(3):
        if edades[x] >= 18:
            mayores += 1
    return mayores


cargar()
print(f"Cantidad mayores a 18: {comparar()}")

