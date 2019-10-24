#PE3E7 Eduardo Antonio Zapata Valero
#Pida al usuario tres número que serán el día, mes y año. Comprueba que la
#fecha introducida es válida.  Por ejemplo: 
#32/01/2017->Fecha incorrecta
#29/02/2017->Fecha incorrepcta
#30/09/2017->Fecha correcta.
dia=int(input("Introduce el dia de una fecha correcta\n"))
mes=int(input("Intrudoce el mes en formato numerico\n"))
año=int(input("Introduce el año\n"))
if (dia==0)or(dia>31)or(mes==0)or(mes>12)or(año<=0):
    print(dia, mes, año, "Fecha incorrecta")
elif(dia>0)and(dia<=30)and(mes==4)or(mes==6)or(mes==9)or(mes==11):
        print (dia, mes, año, "Fecha correcta")
elif (dia>=1)and(dia<=28)and(mes==2):
        print(dia, mes, año,"Fecha correcta")
elif (dia>0)and(dia<=31)and(mes==1)or(mes==3)or(mes==5)or(mes==7)or(mes==8)or(mes==10)or(mes==12):
        print(dia, mes, año, "Fecha correcta")
else:
    print ("Fecha incorrecta")
