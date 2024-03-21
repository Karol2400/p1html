#Problema: determinar si una persona obtuvo o no su licencia de conducir
#Obtener los datos de la persona
Nombre=input("¿Cuál es su nombre? ")
print("")
Edad=int(input("¿Cuál es su edad? "))
print("")
Calificacion=float(input("¿Cuál es la calificacion de su examen? "))
print("")
#Comparar datos y determinar si la persona obtuvo o no su licencia de conducir
if Edad >= 18 and Calificacion >=7 :
    print ("Felicidades", Nombre, "usted obtuvo su licencia de conducir")
    print("")
else:
    print ("Lo sentimos", Nombre, "usted no pudo obtener tu licencia para conducir")
    print("")
#Obtener datos de la identificacion
Indentificacion=input("¿Que comprobante de identificacion prsentaste? ").upper()
#Comparar datos y determinar si la persona obtuvo o no su licencia de conducir
if (Indentificacion == "Credencial" .upper() or Indentificacion == "Pasaporte" .upper()) :
    print ("Documento aceptado")
    print("")
else:
    print ("Lo sentimos, debe presentar otro documento")
    print("")
