#Escribe un programa que pida una frase,
#y pase la frase como parámetro a una
#función que debe eliminar los espacios
#en blanco (compactar la frase).
#El programa principal imprimirá
#por pantalla el resultado final.

def quitaEspacios(x):
    x=x.replace(" ","")
    return x

frase=input("Indica una frase: ")
resultado=quitaEspacios(frase)
print(resultado)
