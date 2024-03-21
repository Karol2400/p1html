import os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

clear()

print("Hola bienvenido a mi codigo")
print("")
n1=float(input("Inserte un numero "))
n2=float(input("Inserte un numero "))
print("")
S=n1+n2
R=n1-n2
R1=n2-n1
D=n1/n2
D1=n2/n1
M=n1*n2
print("La suma de esos dos numero es ",S)
print("La Resta de esos dos numero es ",R, ";", n1, "-", n2)
print("La Resta de esos dos numero es ",R1, ";", n2, "-", n1)
print("La division de esos dos numero es ",D, ";", n1, "/", n2)
print("La division de esos dos numero es ",D1, ";", n2, "/", n1)
print("La muliplicacion de esos dos numero es ",M)
print("")
n3=float(input("Inserte un numero "))
n4=float(input("Inserte un numero "))
n5=float(input("Inserte un numero "))
print("")
Ss=S+n3+n4+n5
print("La suma de esos cinco numero es ",Ss)
print("")
print("")