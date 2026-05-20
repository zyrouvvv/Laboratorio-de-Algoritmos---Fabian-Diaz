#5. Se ingresa por teclado un valor entero, mostrar una leyenda que indique si el número es positivo, negativo o nulo (es decir cero).

num = int(input("Ingrese un valor entero: "))

if num > 0:
    print("Su valor es positivo")

if num < 0:
    print("Su valor es negativo")

if num == 0:
    print("Su valor es nulo")
