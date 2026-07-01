"""4- Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias."""

def carga():
    candidatos = []
    
    cantidad = int(input("Ingrese la cantidad de candidatos: "))
    for x in range(cantidad):
        nombre = input(f"Ingrese el nombre del candidato {x+1}")
        
        provincias = []
        cantidadProv = int(input("Cantidad de provincias:  "))

        for j in range(cantidadProv):
            provincia = input("Ingrese la provincia:  ")
            votos = int(input("Ingrese la cantidad de votos: "))

            provincias.append((provincia, votos))
            candidatos.append([nombre, provincias])

            return candidatos
        
def imprimir(candidatos):
    for candidato in candidatos:
        total = 0

        for provincia in candidato[1]:
            total += provincia[1]
        print(candidato[0], "tiene", total, "votos")
    
candidatos = carga()
imprimir(candidatos)