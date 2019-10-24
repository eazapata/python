#PE5E6
#Escribe un programa que pida
#la altura de un triángulo y lo dibuje de la siguiente manera:
alt=int(input("Introduce la altura del triangulo\n"))
for i in range (alt):
    print(" ")
    for j in range (i+1):
        print ("*",end="")
        
