#Escribe un programa que pida un texto por pantalla,
#este texto lo pase como parámetro a un procedimiento,
#y éste lo imprima primero todo en minúsculas y
#luego todo en mayúsculas.
def minmay(texto=input("Introduce un texto: ")):
    print (texto.upper())
    print(texto.lower())

minmay()

    
