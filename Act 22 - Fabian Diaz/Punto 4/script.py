def cargar_catalogo():
    planetas = {}

    for i in range(4):
        nombre = input("Nombre del exoplaneta: ")
        distancia = float(input("Distancia en años luz: "))
        atmosfera = input("Tipo de atmósfera: ")
        habitable = input("Es habitable? (si/no): ")

        if habitable == "si":
            habitable = True
        else:
            habitable = False

        planetas[nombre] = (distancia, atmosfera, habitable)

    return planetas


def buscar_exoplaneta(planetas):
    nombre = input("Ingrese nombre del exoplaneta: ")

    if nombre in planetas:
        distancia, atmosfera, habitable = planetas[nombre]

        print("Distancia:", distancia)
        print("Atmósfera:", atmosfera)
        print("Habitable:", habitable)
    else:
        print("El exoplaneta no figura en el catálogo actual")


def reportar_habitables(planetas):
    print("Exoplanetas habitables:")

    for nombre in planetas:
        distancia, atmosfera, habitable = planetas[nombre]

        if habitable == True:
            print(nombre)


planetas = cargar_catalogo()
buscar_exoplaneta(planetas)
reportar_habitables(planetas)