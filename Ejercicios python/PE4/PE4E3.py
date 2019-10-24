#PE4E3 Eduardo Antonio Zapata Valero
#Pida al usuario si quiere calcular el área de un triángulo o un cuadrado,
#y pida los datos según que caso y muestre el resultado.
fig=(input("Quieres calcular el área de un triángulo (t) o de un cuadrado (c) "))
if (fig=="t"):
    print ("Ha elegido triángulo, introduce base y altura del triángulo\n")
    b=float(input())
    h=float(input())
    print("El área del triángulo es ",(b*h)/2)

elif(fig=="c"):
    l=float(input("Has elegido cuadrado, introduce el valor del lado\n"))
    print("El área del cudrado es ",(l*l))
else:
    print("No se reconoce la figura que de la que quieres sacar el área")
    

    
