"""2. Confeccionar una función que reciba tres enteros y los muestre ordenados
de menor a mayor. En otra función solicitar la carga de 3 enteros por
teclado y proceder a llamar a la primer función definida."""


def ordenar(valor1,valor2,valor3):
    if valor1 < valor2 and valor1 < valor3 and valor2 < valor3:
        print("ordenado de menor a mayor: ", valor1,valor2,valor3)
    else:
        if valor1<valor1 and valor1<valor3 and valor3<valor2:
            print("ordenado de menor a mayor: ", valor1,valor3,valor2)
        else:
            if valor2<valor1 and valor2<valor3 and valor1<valor3:
                print("ordenado de menor a mayor: ", valor2,valor1,valor3)
            else:
                if valor2<valor1 and valor2<valor3 and valor1>valor3:
                    print("ordenado de menor a mayor: ", valor2,valor3,valor2)
                else:
                    if valor3<valor1 and valor3<valor2 and valor1<valor2:
                        print("ordenado de menor a mayor: ", valor3,valor1,valor2)
                    else:
                        print("ordenado de menor a mayor: ", valor3,valor2,valor1)

def cargar():
    valor1=int(input("Ingrese el primer valor"))
    valor2=int(input("Ingrese el segundo valor"))
    valor3=int(input("Ingrese el tercer valor"))
    ordenar(valor1,valor2,valor3)
    
cargar()
                        