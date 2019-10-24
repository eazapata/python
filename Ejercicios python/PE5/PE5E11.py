#Escribe un programa que pida un número e imprima todos sus divisores.
num=int(input("Introduce un número"))
if num==0:
    print("Número incorrecto\n")
else:    
    print("Los divisores de ", num, "son :",end=" ")
    for i in range (1,num+1):
        if num%i==0:
            print(i, end=" ")
    
