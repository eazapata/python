#Escribe un programa que te pida primero un
#número y luego te pida números hasta que
#la suma de los números introducidos coincida
#con el número inicial. El programa termina
#escribiendo la lista de números.
limite=int(input("Escribe limite: "))
suma=0
lista=[]
while (suma<limite):
    num=int(input("Escribe un valor: "))
    while((num+suma)>limite):
        num=int(input("%d es demasiado grande escribe otro valor: "%num))
    lista+=[num]
    suma+=num
print("El limite a superar es %d"%(limite),end="")
print(", la lista creada es: ",end="")
for i in range(len(lista)):
    if i==len(lista)-1:
         print(lista[i],end="")
    else:
         print(lista[i],",",end="")
