Edad=int(input("¿Cuál es su edad? "))
print("")
if Edad >= 18 :
    print ("Mayor de edad")
    print("")
else:
    print ("Menor de edad")
    print("")
Calificacion=int(input("¿Cuál es la calificacion de su examen? "))
print("")
if Calificacion >= 6 :
    print ("Aprobo")
    print("")
else:
    print ("Reprobo")
    print("")
Estatura=float(input("¿Cuál es su estatura? "))
print("")
if Estatura < 1.20 :
    print ("bajito")
    print("")
elif Estatura>=1.21 and Estatura<1.40 :
    print ("medianito")
    print("")
elif Estatura>=1.41 and Estatura<1.69 :
    print ("alto")
    print("")
else:
    print ("desconocida")
    print("")