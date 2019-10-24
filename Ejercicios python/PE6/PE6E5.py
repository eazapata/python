#PE6E5
#Escribe un programa que te pida números cada vez más grandes
#y que se guarden en una lista. Para acabar de escribir
#los números, escribe un número que no sea mayor que el anterior.
#El programa termina escribiendo la lista de números:
num1=int(input("Escribe un número"))
num2=int(input("Escribe un número mayor que %d"%(num1)))
lista=[num1]
while num1<num2:
    lista+=[num2]
    num2=int(input("Escribe un número mayor que %d"%(num2)))
    print("Has introducido los siguientes números ",end="")
    for i in range(len(lista)):
        if i>= len(lista)-1:
            print(lista[i],end="")
        else:
            print(lista[i],",",end="")
        


