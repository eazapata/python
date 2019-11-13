#Escribe un programa que te pida una frase,
#y pase la frase como parámetro a una función.
#Ésta debe devolver si es palíndroma o no ,
#y el programa principal escribirá el
#resultado por pantalla:
def palindroma(string):
    if (string.replace(" ","")==string.replace(" ","")[::-1]):
       palin=print(string,"es palíndroma")
    else:
        palin=print(string,"no es palíndroma")
    return (palin)
frase=input("Dime algo: ")
palindroma(frase)
