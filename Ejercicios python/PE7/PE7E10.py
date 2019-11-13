#Escribe un programa que te pida una palabra o número,
#pase por parámetro estos datos a una función, y ésta te
#diga si es o no palíndroma o capicúa. El programa
#principal imprimirá el resultado de la función:
resul=""
def capicua(x):
    if (x==x[::-1]):
        resultado=print(x,"es capicúa o palíndroma")
    else:
         resultado=print(x,"no es capicúa o palíndroma")
    return (resultado)


valor=input("Dime algo: ")
resul=(capicua(valor))
