#Escribe un programa que pida un número (límite)
#y luego te pida números hasta que la suma de los
#números introducidos supere el límite inicial.
#El programa termina escribiendo la lista de números.
limite=int(input("Escribe limite: "))
suma=0
suma1=0
lista=[]
while (suma<=limite):
    num=int(input("Escribe un valor: "))
    suma+=num
    lista+=[num]
print("El limite a superar es %d"%(limite),end="")
print(", la lista creada es: ",end="")
for i in range(len(lista)):
    if i==len(lista)-1:
         print(lista[i],end="")
    else:
         print(lista[i],",",end="")
print(", ya que la suma de estos números es: ",suma)

    
        
