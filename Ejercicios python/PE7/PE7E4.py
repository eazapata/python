#Escribe un programa que pida una frase, y le pase como
#parámetro a una función dicha frase. La función debe
#sustituir todos los espacios en blanco de una frase
#por un asterisco, y devolver el resultado para que el
#programa principal la imprima por pantalla.


def quitaespacio(x):
    x=x.replace(" ","*");
    return (x)

frase=str(input("Escribe una frase: "))
sinespacios=quitaespacio(frase)
print(sinespacios)
