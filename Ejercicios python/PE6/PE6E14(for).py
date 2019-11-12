#Desarrolla un programa junto con tu compañero, apoyándote en la
#“metodología pair programming” que tenga las siguientes características:
#Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
#Dicho problema resuélvelo con bucles for y while. 
#Justifica en el propio programa porque una opción es adecuada y la otra no.
#¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará
#que efectivamente una solución es más eficiente? Investiga para comprobarlo.
lista=[]
asig=int(input("Cuantas asignaturas tienes"))
aprob=0
for i in range (asig):
    nota=int(input("Introduce las notas: "))
    lista.append(nota)
for i in range (len(lista)):
    if (lista[i]<5):
        aprob+=1
if aprob>0:
    print ("Vas a repetir")
else:
    print("Pasa de curso")
    
