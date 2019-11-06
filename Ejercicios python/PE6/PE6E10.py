#Escribe un programa que te pida los nombres y notas de alumnos.
#Si escribes una nota fuera del intervalo de 0 a 10, el programa
#entenderá que no quieres introducir más notas de este alumno.
#Si no escribes el nombre, el programa entenderá que no quieres introducir más alumnos.
#Nota: La lista en la que se guardan los nombres y notas tiene
#esta estructura [[nombre1, nota1, nota2, etc], [nombre2, nota1, nota2, etc],
#[nom3, nota1, nota2, etc], etc]
principal=[]
lista=[]
aux=[]
nota=1
nom=("a")
while(nom!=("")):
    nom=input("Escribe el nombre del alumno: ")
    lista.append(nom)
    if(nom!=("")):
        nota=int(input("Introduce una nota: "))
        while (nota>10):
            nota=int(input("Número no válido introduce otro: "))
        lista.append(nota)
        while (nota>=0)and(nota<=10):
            nota=int(input("Introduce otra nota: "))
            lista.append(nota)
    del lista[-1]
    aux=(lista)
    principal.append(lista)
    lista=[]
print("Las notas de los alumnos son: ")
for i in range(len(principal)):
    for j in range (len(principal[i])):
        if(j==(len(principal[i])-1)):
            print (principal[i][j])
        else:
            print(principal[i][j],end="")
        
        
