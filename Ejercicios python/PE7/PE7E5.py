#Escribe un programa que te pida una frase y una vocal,
#y pase estos datos como parámetro a una función que se
#encargará de cambiar todas las vocales de la frase por
#la vocal seleccionada. Devolverá la función la frase modificada,
#y el programa principal la imprimirá:
vocales=["a","e","i","o","u"]
def cambialetra(a,b,c):
    for i in range (len(a)):
        if a[i] in c:
            a=a.replace(a[i],b)
    return a
frase=str(input("Indica una frase: "))
vocal=str(input("Indica una vocal: "))

cambiada=cambialetra(frase,vocal,vocales)
print(cambiada)
            
