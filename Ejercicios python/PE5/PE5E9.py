#PE5E9
#Escribe un programa que pida la anchura
#y la altura de un rectángulo y lo dibuje de la siguiente manera:
print("Introduce la altura y la anchura del rectangulo\n")
alt=int(input())
anch=int(input())
if alt==0 or anch==0:
    print("Valores invalidos")
else:
    print ("*"*anch)
    alt=alt-2
    for i in range (alt):
        print ("*"+(" "*(anch-2)+"*"))
print ("*"*anch)

       
            
   
        
 
