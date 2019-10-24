#PE4E2 Eduardo Antonio Zapata Valero
#Pida al usuario 5 números y diga si estos estaban en orden decreciente,
#creciente o desordenados.
print("Introduce 5 números ")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
if (num1<num2)and(num2<num3)and(num3<num4)and(num4<num5):
    print("La lista es creciente")
elif (num1>num2)and(num2>num3)and(num3>num4)and(num4>num5):
    print ("La lista es decreciente")
else:
    print("desordenados")
