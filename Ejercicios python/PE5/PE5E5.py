#PE5E5
#Escribe un programa que pida la altura y
#ancho de un rectángulo y lo dibuje de la siguiente manera:
print("Introduce la altura y el ancho de un rectángulo")
altura=int(input())
ancho=int(input())
for i in range(altura):
    print (" ")
    for j in range(ancho):
        print ("*",end="")
        
