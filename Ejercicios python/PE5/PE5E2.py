#PE5E2 Eduardo Antonio Zapata Valero
#Escribe un programa que pida dos números y escriba qué números
#entre ese par de números son pares y cuáles impares
print("Introduce 1 numero")
num1=int(input())
print("Introduce 1 numero mayor que el anterior")
num2=int(input())
for i in range(num1,num2):
    if (i%2==0):
        print("El número es par")
    else:
        print("El múmero es impar")
    
