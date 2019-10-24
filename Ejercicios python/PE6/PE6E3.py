#PE6E3
#Escribe un programa que pida notas y los guarde en una lista.
#Para terminar de introducir notas, escribe una nota que
#no esté entre 0 y 10. El programa termina escribiendo la
#lista de notas.
lista=[]
nota=float(input("Escribe una nota"))
while nota>0 and nota<=10:
    lista+=[float(nota)]
    nota=float(input("Escribe una nota"))
print("Las notas que has escrito son",lista)
