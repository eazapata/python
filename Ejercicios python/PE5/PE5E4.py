#PE5E4 Eduardo Antonio Zapata Valero
#Escribe un programa que pida un número y calcule su factorial.
num=int(input("Introduce el número del que quieres sacar el factoria\n"))
factorial=1
for i in range(1,num+1):
        factorial=i*factorial
print("El factorial de",num,"es",factorial)
