def cargar_registro():
    amenazas = {}

    for i in range(4):
        ip = input("Ingrese IP: ")
        dispositivo = input("Nombre del dispositivo: ")
        intentos = int(input("Intentos fallidos: "))

        amenazas[ip] = (dispositivo, intentos)

    return amenazas


def listar_amenazas(amenazas):
    print("Lista de amenazas:")

    for ip in amenazas:
        dispositivo, intentos = amenazas[ip]
        print("IP:", ip)
        print("Dispositivo:", dispositivo)
        print("Intentos:", intentos)


def filtrar_bloqueos(amenazas):
    print("IPs a bloquear:")

    for ip in amenazas:
        dispositivo, intentos = amenazas[ip]

        if intentos > 5:
            print(ip)


amenazas = cargar_registro()
listar_amenazas(amenazas)
filtrar_bloqueos(amenazas)