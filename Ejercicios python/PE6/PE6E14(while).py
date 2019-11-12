#Desarrolla un programa junto con tu compañero, apoyándote en la
#“metodología pair programming” que tenga las siguientes características:
#Piensa en un problema que requiera para su resolución el uso de sentencias repetitivas.
#Dicho problema resuélvelo con bucles for y while. 
#Justifica en el propio programa porque una opción es adecuada y la otra no.
#¿Crees que si medimos el tiempo de ejecución de ambas soluciones demostrará
#que efectivamente una solución es más eficiente? Investiga para comprobarlo.
lista=[]
asig=int(input("Cuantas asignaturas tienes"))
nota=10
while asig!=0 and nota>=5:
    nota=int(input("Introduce una nota "))
    asig-=1
if asig==0:
    print('No repites crack')
else:
    print('Repites crack')


