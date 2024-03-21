#Realizar las cuatro operaciones basicas de 2 numeros solicitados al usuario


print("Hola bienvenido a mi codigo")
print("")
Nombre=input("¿Cuál es tu nombre? ")
print("")
print ("Muy bien", Nombre, "comenzemos")
print("")
Operacion=100
while Operacion :
    n1=float(input("Inserta un numero "))
    print("")
    n2=float(input("Inserta un numero "))
    print("")
    SUMAR=n1+n2
    RESTAR=n1-n2
    DIVIDIR=n1/n2
    MULTIPLICAR=n1*n2
    print("1 - SUMAR")
    print("2 - RESTAR")
    print("3 - MULTIPLICAR")
    print("4 - DIVIDIR")
    print("5 - Salir")
    print("")
    Operacion=int(input("¿Qué operacion deseas realizar? "))
    if Operacion == 1:
        print(SUMAR)
        print("")
    elif Operacion == 2:
        print(RESTAR)
        print("")
    elif Operacion == 3:
        print(MULTIPLICAR)
        print("")
    elif Operacion == 4:
        print(DIVIDIR)
        print("")
    elif Operacion == 5:
        print("")
        print("Gracias", Nombre, "hasta luego")
        print("")
        break
    else:
        print("")
        print("ERROR")
        print("")