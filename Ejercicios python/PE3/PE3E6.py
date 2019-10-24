#PE3E5 Eduardo Antonio Zapata Valero
#Pida al usuario el precio de un producto y el nombre
#del producto y muestre el mensaje con el precio del IVA (21%).
#Por ejemplo: “ Tu bicicleta vale 100 euros y con el 21 % de
#IVA se queda en 121 euros en total”.

niva=float(input("Indica el precio del producto sin iva"))
print("El producto que has comprado vale",  niva,"y con el 21% de IVA se queda en", ((niva*21)/100+niva))
