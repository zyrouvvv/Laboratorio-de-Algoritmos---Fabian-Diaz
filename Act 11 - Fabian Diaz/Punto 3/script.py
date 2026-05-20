#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1 = int(input("Ingrese el primer valor: "))
num2 = int(input("Ingrese el segundo valor: "))

if num1 > num2:
    suma = num1 + num2 
    diferencia = num1 - num2
    print(f"La suma del valor 1 y el valor 2 es {suma} y la diferencia es de {diferencia}")

else:
    producto = num1 * num2
    division = num1 / num2
    print(f"La multiplicacion entre el valor 1 y el valor 2 es {producto} y la division es {division}")