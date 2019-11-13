#Escribir un programa que lea una frase,
#y pase ésta como parámetro a una función
#que debe contar el número de palabras que
#contiene. Debe imprimir el programa principal
#el resultado. Asumir que cada palabra está
#separada por un solo blanco:
#Asumir que cada palabra está separada por un solo blanco.
#No se sabe cómo están separadas las palabras. Pueden
#estar separadas por más de un blanco o por signos de puntuación.

def cuenta(frase,lista):
    count=frase.split()
    lista2=[]
    for i in range(0,len(count),1):
        if (count[i] in lista)==False:
            lista2.append(count[i])
    resul=len(lista2)        
    return resul
            





#count=0
lista=[",",";",".",":","?","¿","¡","!"]

frase=input("Dime algo: ")
result=print(cuenta(frase,lista))
