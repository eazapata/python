#PE4E1 Eduardo Antonio Zapata Valero
#Pida al usuario 5 números y diga cual es el mayor y cuál el menor.
print("Introduce 5 números: ")
num1=int(input())
num2=int(input())
num3=int(input())
num4=int(input())
num5=int(input())
mini=num1
maxi=num1
if (num1<mini):
    mini=num1
if(num2<mini):
    mini=num2
if(num3<mini):
    mini=num3
if(num4<mini):
    mini=num4
if(num5<mini):
    mini=num5
if(num1>maxi):
    maxi=num1
if(num2>maxi):
    maxi=num2
if(num3>maxi):
    maxi=num3
if (num4>maxi):
    maxi=num4
if(num5>maxi):
    maxi=num5
print ("El mayor es ", maxi, "y el menor ", mini)
