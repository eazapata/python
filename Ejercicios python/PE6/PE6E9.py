#Escribe un programa que te pida nombres de personas
#y sus números de teléfono. Para terminar debe pulsar “S”
#cuando te pida el nombre. El programa termina escribiendo
#nombres y números de teléfono. Nota: La lista en la que se
#guardan los nombres y números de teléfono tiene esta
#estructura[[nombre1, telef1], [nombre2, telef2], [nom3, telef3], etc],
#es decir, lista de listas.
listanom=[]
listanum=[]
nom=("a")
while(nom!="s"):
    nom=input("Escribe un nombre (escribe una 's' para terminar): ")
    listanom.append(nom)
    if nom!="s":
        num=int(input("Escribe un número de télefono: "))
        listanum+=[num]
print("Los nombres y teléfonos de la agenda son:")
for i in range(len(listanom)-1):
    print(" ")
    print(listanom[i],":",listanum[i])
   
    

        

