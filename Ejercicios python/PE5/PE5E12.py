#Escribe un programa que pida un número y escriba si primo o no
num=int(input("Introduce un numero"))
prim=0
if num==0:
    print("Número incorrecto")
else:
    for i in range (2,num):
        if num%i==0:
            prim=1
    if prim==1:
        print("El número ",num,"no es primo")
    else:
        print("El número ",num,"es primo")

