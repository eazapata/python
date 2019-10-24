#P6E2
#Escribe un programa que te pida números y los guarde en una lista.
#Para terminar de introducir número, simplemente escribe “Salir”.
#El programa termina escribiendo la lista de números.
lista=[]
num=int(input("Introduce un número\n"))
while num!="salir":
    lista+=[num]
    num=input(("Introduce otro número\n"))
print(lista)
