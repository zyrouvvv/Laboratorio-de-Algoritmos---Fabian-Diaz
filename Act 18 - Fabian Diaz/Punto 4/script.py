"""4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras &#39;a&#39; o &#39;A&#39;."""

def contador(cadena):
    contador = 0
    for letra in cadena:
        if letra == "o" or letra == "o":
            contador += 1
    return contador
texto = input("Ingrese un texto: ")
  
print("La cantidad de letras 'o' o 'O' en el texto es: ", contador(texto))