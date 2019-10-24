#PE4E5 Eduardo Antonio Zapata Valer
#Pida al usuario un importe en euros y diga si el cajero automático le
#puede dar dicho importe utilizando el mismo billete y el más grande
#(recuerda que el billete puede ser de 500, 200, 100, 50, 20, 10 y 5 	€).
imp=int(input("Introduce el importe que quieres obtener\n"))
if (imp%500==0):
    (print("El cajero devuelve ",int(imp/500), "billetes de 500 euros"))
elif(imp%200==0):
     print("El cajero devuelve ",int(imp/200), "billetes de 200 euros")
elif(imp%100==0):
     print("El cajero devuelve ",int(imp/100), "billetes de 100 euros")
elif(imp%50==0):
     print("El cajero devuelve ",int(imp/50), "billetes de 50 euros")
elif(imp%20==0):
     print("El cajero devuelve ",int(imp/20), "billetes de 20 euros")
elif(imp%10==0):
     print("El cajero devuelve ",int(imp/10), "billetes de 10 euros")
elif(imp%5==0):
     print("El cajero devuelve ",int(imp/5), "billetes de 5 euros")
else:
    print("no se puede sacar ese importe")
     
        
