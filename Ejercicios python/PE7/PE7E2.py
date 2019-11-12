#Escribe un programa que lea el nombre y los dos
#apellidos de una persona (en tres cadenas de
#caracteres diferentes), los pase como parámetros
#a una función, y ésta debe unirlos y devolver una
#única cadena. La cadena final la imprimirá el
#programa por pantalla.
nom=input("Dime tu nombre: ")
ape1=input("Dime tu primer apellido: ")
ape2=input("Dime tu segundo apellido: ")
nombre=("")
def unir(a,b,c):
    nombre=a+" "+b+" "+c
    return nombre
nombre=unir(nom,ape1,ape2)
print (nombre)
