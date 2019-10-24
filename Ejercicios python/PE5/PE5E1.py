#PE5E1
#Escribe un programa que escriba a los siguientes número
#(la separación entre número es para facilitar cuántos números se deben
#escribir en cada bucle) y en el que la función range que utilices tenga un ÚNICO argumento y
#que el valor de este se corresponda con el número de elementos que aparecen en la lista
#( por Ejemplo, para la primera lista range (10)).
for i in range (10):
    i=i+1
    print("Nº", i," ",end=" ")
print("")
for i in range (10):
    i=(i+1)*2
    print("Nº", i," ",end=" ")
print("")
for i in range(10):
    i=((i+1)*2)+18
    print("Nº", i," ",end=" ")
print("")   
for i in range(6):
    i=10+(i*4)
    print("Nº", i," ",end=" ")
print("")
for i in range(9):
    i=40-(i*5)
    print("Nº", i," ",end=" ")
