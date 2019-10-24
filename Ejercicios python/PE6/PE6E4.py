#PE6E4
#Escribe un programa que te pida dos números,
#de manera que el segundo sea mayor que el primero
num1=int(input("Introduce un número"))
print("Introduce un número mayor que",num1,"\n")
num2=int(input())
while num2<num1:
    num2=int(input("El número no es mayor que %d introduce un número mayor que %d\n"%(num1,num2)))
print("Los números que has escritos son",num1,"y",num2)
