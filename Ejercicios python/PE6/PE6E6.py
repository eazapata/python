 #Escribe un programa que pida primero dos números
#(máximo y mínimo) y que después te pida números intermedios.
#Para terminar de escribir números, escribe un número que no
#esté comprendido entre los dos valores iniciales.
#El programa termina escribiendo la lista de números.
lista=[]
mini=int(input("Introduce el número que será el mínimo"))
maxi=int(input("Introduce el número que será el máximo"))
while(maxi<mini):
    maxi=int(input("%d no es mayor que %d"%(maxi,mini)))

num1=int(input("Introduce un número que esté entre los anteriores"))
lista+=[num1]
while (num1>mini) and (num1<maxi):
    num2=int(input("Introduce un número que esté entre los anteriores"))
    num1=num2
    lista+=[num1]
print("Los números entre %d y %d son: "%(mini,maxi))
for i in range(len(lista)-1):
    if i==len(lista)-2:
         print(lista[i])
    else:
         print(lista[i],",",end="")    

