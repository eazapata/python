#Escribe un programa que pida dos palabras
#las pase como parámetro a un procedimiento
#y diga si riman o no. Si coinciden las tres
#últimas letras tiene que decir que riman.
#Si coinciden sólo las dos últimas tiene que
#decir que riman un poco y si no, que no riman.

def rimar(a,b):
    if a[-3:]==b[-3:]:
        resul=print("Las palabras riman")
    elif a[-2:]==b[-2:]:
        resul=print("Las palabras riman un poco")
    else:
        resul=print("Las palabras no riman")

    
pala1=input("Indica una palabra: ")
pala2=input("Indica otra palabra: ")
rimar(pala1,pala2)
