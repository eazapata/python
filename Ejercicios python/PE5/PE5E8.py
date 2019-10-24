#PE5E8
#Escribe un programa que pida
#la anchura de un triángulo y lo dibuje de la siguiente manera:
alt=int(input("Introduce la altura del triangulo\n"))
for i in range (alt):
    print((i+1)*"*")
for i in range (alt):
    print((alt-1)*"*")
    alt=alt-1
