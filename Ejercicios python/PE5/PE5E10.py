#Escribe un programa que pida la altura de un
#triángulo y lo dibuje de la siguiente
#manera:
alt=int(input("Introduce la altura del triangulo\n"))
simb=("*")
for i in range (alt):
    print (" "*(alt-1)+simb)
    simb=simb+"**"
    alt=alt-1
    
        
   
        
        
   
   
