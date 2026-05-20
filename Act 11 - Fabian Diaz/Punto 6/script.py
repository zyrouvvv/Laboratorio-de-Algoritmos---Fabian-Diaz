#6. De un operario se conoce su sueldo y los años de antigüedad. Se pide confeccionar un programa que lea los datos de entrada e informe: 
# a. Si el sueldo es inferior a 500 y su antigüedad es igual o superior a 10, otorgarle un aumento del 20 %, mostrar el sueldo a pagar. 
# b. Si el sueldo es inferior a 500 pero su antigüedad es menor a 10 años, otorgarle un aumento de 5 %. 
#c. Si el sueldo es mayor o igual a 500 mostrar el sueldo en pantalla sin cambios.

sueldo = int(input("Ingrese su sueldo: "))
antiguedad = int(input("Ingrese sus años de antiguedad: "))

if sueldo < 500 and antiguedad >= 10:
    aumento20 = sueldo*1.2
    sueldo1 = sueldo + aumento20
    print(f"Usted va a recibir un aumento del 20%: {aumento20} y quedara como sueldo final: {sueldo1}")
else:
    aumento5 = sueldo * 1.05
    sueldo2 = sueldo + aumento5
    print(f"Usted va a recibir un aumento del 5%: {aumento5} y quedara como sueldo final: {sueldo2}")
if sueldo >= 500:
    print(f"Su sueldo seguira siendo: {sueldo}")






