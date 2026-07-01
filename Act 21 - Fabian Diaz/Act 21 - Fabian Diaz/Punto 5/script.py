"""5-
Almacenar los nombres de 5 productos y sus precios. Utilizar una lista y cada
elemento una tupla con el nombre y el precio.
Desarrollar las funciones:
1) Cargar por teclado.
2) Listar los productos y precios.
3) Imprimir los productos con precios comprendidos entre 10 y 15"""

def carga():
    productos = []

    for x in range (5):
        nombre = input(f"Ingrese el productos {x+1}")
        precio = int(input(f"Ingrese el precio del producto {x+1}"))

        productos.append((nombre, precio))

    return productos

def listarProductos(productos):
    for producto in productos: 
        print("Productos", producto[0], "Precio", producto[1])

def precios1015(productos):
    print("Productos entre 10 y 15")

    for producto in productos:
        if producto[1] >= 10 and producto[1] <= 15:
            print(producto[0])

productos = carga()
listarProductos(productos)
precios1015(productos)