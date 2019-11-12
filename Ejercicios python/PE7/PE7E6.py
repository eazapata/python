#Escribe un programa que lea el nombre de una persona y un carácter,
#le pase estos datos a una función que comprobará si dicho carácter
#está en su nombre. El resultado de dicha función lo imprimirá el
#programa principal por pantalla.

def cambialetra(a,b):
    if b in a:
        resultado=("El cáracter aparece en el nombre")
    else:
        resultado=("El cáracter no aparece en el nombre")
    return resultado

nombre=str(input("Indica tu nombre: "))
vocal=str(input("Indica una vocal: "))

resultado=cambialetra(nombre,vocal)
print(resultado)
