#PE3E5 Eduardo Antonio Zapata Valero
#Pida un número que como máximo tenga tres cifras
#(por ejemplo serían válidos 1, 99 i 213 pero no 1001).
#Si el usuario introduce un número de más de tres cifras debe un
#informar con un mensaje de error como este “ ERROR: El número 1005 tiene más de tres cifras”.
num=int(input("Introduce un número, no puede tener más de 3 cifras\n"))
if (num>=1000):
    print ("Error",(num), "es un número con más de tres cifras")
else:
    print("Tu número es: \n",num)
