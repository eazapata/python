#PE5E3 Eduardo Antonio Zapata Valero
#Escribe un programa que pida dos números
#y escriba la suma de enteros desde el primero hasta el último.
print ("Ingresa un número:\n")
num1=int(input())
print("Ingresa un número mayor que el anterior:\n")
num2=int(input())
suma=0
if (num1>num2):
    print("El número",num1,"es mayor que",num2)
else:
    if(num2-num1==1):
        print(num1,"+",num2,"=",(num1+num2))
    else:
        for i in range(num1,num2):
            suma=i+suma
            print(i,"+",end="")
    suma=suma+num2    
    print(num2,"=",suma)
