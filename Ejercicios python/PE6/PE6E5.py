#PE6E5
#Escribe un programa que te pida números cada vez más grandes
#y que se guarden en una lista. Para acabar de escribir
#los números, escribe un número que no sea mayor que el anterior.
#El programa termina escribiendo la lista de números:
lista=[]
num1=int(input("Escribe un número 2"))
lista+=[num1]
num2=int(input("Escribe un número mayor que %d "%(num1)))
lista+=[num2]
while num1<num2:
    num1=num2
    num2=int(input("Escribe un número mayor que %d "%(num2)))
    lista+=[num2]
for i in range(len(lista)-1):
    if i==len(lista)-2:
         print(lista[i])
    else:
         print(lista[i],",",end="")
   


