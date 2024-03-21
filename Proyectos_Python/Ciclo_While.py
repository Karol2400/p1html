#Programa que te pregunta tu edad hasta que escribes 0
Edad=100
while Edad > 0 :
    Edad=int(input("¿Cuál es tu edad? "))
    if Edad > 100 :
        print("Tu edad no es valida")
    else:
        print("")
        break