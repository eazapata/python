#PE4E4 Eduardo Antonio Zapata Valero
#Pida al usuario tres números y un cuarto número, y
#compruebe si éste último es divisor de los tres números primeros.
print("Introduce 3 números y un cuarto para comprobar si es divisor")
num1=int(input())
num2=int(input())
num3=int(input())
div=int(input())
if (num1%div==0)and(num2%div==0)and(num2%div==0):
    print("El cuarto número es divisor de los anteriores")
else:
    print("El cuarto número no es divisor de los anteriores")
