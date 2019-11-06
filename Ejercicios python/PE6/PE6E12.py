#Escribir un programa para jugar a adivinar un número
#(el usuario piensa un número y el programa lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número a
#adivinar y luego intenta adivinar de qué número se trata.
#El usuario va diciendo si el número que ha dicho el programa es
#menor, mayor o igual al que se ha buscado.
import random
import time
random.seed (time.time ())
minimo=int(input("Valor mínimo: "))
maximo=int(input("Valor máximo: "))
while (minimo>maximo):
    maximo=int(input("%d no es mayor que %d,introduce otro número: "%(maximo,minimo))) 
secreto=int(input("Piensa un número entre %d y %d a ver si lo puedo adivinar"%(minimo,maximo)))
while(secreto<minimo)or(secreto>maximo):
    secreto=int(input("Ese número no está entre %d y %d di otro"%(minimo,maximo)))
num=random.randint (minimo, maximo)
while (num!=secreto):
    while (num<secreto):
        print("Es %d ?:mayor"%(num))
        num=int(random.randint (minimo, maximo))
    while (num>secreto):
        print("Es %d ?:menor"%(num))
        num=int(random.randint (minimo, maximo))
if (num==secreto):
    print("Es %d ?:igual"%(num))
    print("Gracias por jugar")
