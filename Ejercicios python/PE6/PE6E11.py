#Escribir un programa para jugar a adivinar un número
#(el ordenador "piensa" el número y el usuario lo ha de adivinar).
#El programa empieza pidiendo entre qué números está el número a adivinar,
#se "inventa" un número al azar y luego el usuario va probando valores.
#El programa va decidiendo si son demasiado grandes o pequeños. pista:
lista=[]
import random
import time
random.seed (time.time ())
minimo= int (input ( "Valor mínimo:"))
maxi= int (input ( "Valor máximo:"))
secreto = random.randint (minimo, maxi)
print("A ver si adivinas un número entero entre %d y %d."%(minimo,maxi))
num=int(input("Introduce el número"))
while (num!=secreto):
    while(num<secreto):
        num=int(input("El número es demasiado pequeño prueba otra vez"))
        lista.append(num)
    while(num>secreto):
        num=int(input("El número es demasiado grante, prueba otra vez"))
        lista.append(num)
if (num==secreto):
    print("Correcto! Lo has intentado",len(lista)," veces.")
        


        
          
