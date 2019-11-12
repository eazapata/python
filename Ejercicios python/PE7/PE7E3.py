#Escribe un programa que lea una frase,
#y la pase como parámetro a un procedimiento,
#y éste debe mostrar la frase con un carácter
#en cada línea.
frase=str(input("Indica una frase: "))
def caracterlinea(x):
    for i in range (len(x)):
        print(x[i])

caracterlinea(frase)
