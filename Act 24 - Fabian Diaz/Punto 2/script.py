"""2-
En un videojuego multijugador en línea, los jugadores se agrupan en clanes o gremios
para realizar misiones cooperativas.
 Diseñar un diccionario donde la Clave sea el nombre del Gremio (ej:
&quot;DragonesDeFuego&quot;) y el Valor sea una lista de cadenas con los nombres de
los jugadores (nicknames) que lo integran.
Desarrollar las siguientes funciones:
1. Registrar gremios: Cargar por teclado 3 gremios. Para cada gremio, se debe
preguntar cuántos integrantes posee para cargar sus respectivos nombres de
usuario en la lista interna.
2. Listar clanes: Mostrar los nombres de todos los gremios junto a la cantidad total
de miembros que posee cada uno.
3. Buscar jugador: Solicitar por teclado el nombre de un jugador y buscar en qué
gremio está registrado. Informar el gremio encontrado o indicar si el jugador es
&quot;Solitario&quot; (no pertenece a ningún clan)."""


def registrar_gremios():
    gremios = {}

    for i in range(3):
        nombre_gremio = input(f"Ingrese el nombre del gremio {i + 1}: ")
        cantidad = int(input(f"¿Cuántos integrantes tiene {nombre_gremio}? "))
        jugadores = []

        for j in range(cantidad):
            jugador = input(f"Ingrese el nombre del jugador {j + 1}: ")
            jugadores.append(jugador)

        gremios[nombre_gremio] = jugadores

    return gremios


def listar_clanes(gremios):
    print("Lista de gremios: ")

    for gremio, jugadores in gremios.items():
        print(f"Gremio: {gremio} - Cantidad de miembros: {len(jugadores)}")


def buscar_jugador(gremios):
    jugador_buscado = input("Ingrese el nombre del jugador a buscar: ")

    encontrado = False

    for gremio, jugadores in gremios.items():
        if jugador_buscado in jugadores:
            print(f"El jugador {jugador_buscado} pertenece al gremio: {gremio}")
            encontrado = True
            break

    if not encontrado:
        print(f"El jugador {jugador_buscado} es Solitario.")


gremios = registrar_gremios()
listar_clanes(gremios)
buscar_jugador(gremios)
