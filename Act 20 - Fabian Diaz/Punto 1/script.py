"""1. Desarrollar una función que reciba una lista de string y nos retorne el que
tiene más caracteres. Si hay más de uno con dicha cantidad de caracteres
debe retornar el que tiene un valor de componente más baja.
En el bloque principal iniciamos por asignación la lista de string:
palabras=[&quot;enero&quot;, &quot;febrero&quot;, &quot;marzo&quot;, &quot;abril&quot;, &quot;mayo&quot;, &quot;junio&quot;]
print(&quot;Palabra con mas caracteres:&quot;,mascaracteres(palabras))
(La lista debe tener la misma cantidad de elementos, pero los textos los
eligen ustedes)"""


def masCaracteres(palabras):
    for i in range(5):
        mas = palabras[0]
        if len(mas) < len(palabras[i+1]):
            mas = palabras[i]
    
    return mas
        




palabra = ["Hola", "Jueves", "Moto", "Kiwi", "Computadora", "Libro"]
print(f"Palabra con mas caracteres: {masCaracteres(palabra)}")
