#Escribe un programa que lea una frase,
#y la pase como parámetro a un procedimiento.
#El procedimiento contará el número de
#vocales (de cada una) que aparecen,
#y lo imprimirá por pantalla.
vocales=["a","e","i","o","u"]
def cuenta (a,b):
    suma=0
    for i in range (len(a)):
        if a[i] in b:
            suma=suma+1
        else:
            suma=suma
    print("El número de vocales que aparece es ",suma)
    
frase=(input("Indica una frase: "))
cuenta(frase,vocales)

    
