#Desarrolla de nuevo el ejercicio de la
#práctica anterior de los números primos,
#con while. Reflexiona y escribe en el propio
#programa en forma de comentario, qué opción es mejor y por qué.
div=2
resto=("a")
num=int(input("Introduce un número: \n"))
while(div<num) and (resto!=0):
    resto=num%div
    div=div+1
if(num==2):
    print("El número",num,"es primo")
elif(resto==0):
    print("El número",num,"no es primo")
elif(resto!=0):
    print("El número",num,"es primo")
    









