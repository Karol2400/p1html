#Programa que pregunta varios deportes
#Guarda los deportes en una lista
#Variable tipo LISTA
Deportes=[]
#Preguntar ¿Cuantos deportes va a escribir?
Cantidad_Deportes=int(input("¿Cuantos deportes vas a escribir? "))

for i in range(Cantidad_Deportes):
#Preguntar un deporte
    Deporte=input("Escribe un deporte ")
    Deportes.append(Deporte)
for i in (Deportes):
    print(i)
depBorrar=input("¿Cuál deporte deseas borrar? ")
Deportes.remove(depBorrar)
print(i)

Materias=[]
Cantidad_Materia=int(input("¿Cuantas materias llevas en tus estudios academicos? "))
for i in range(Cantidad_Materia):
    Materia=input("Escribe las materias que llevas ")
    Materias.append(Materia)
for i in (Materias):
    print(i)
depBorrar=input("¿Cuál Materia deseas borrar? ")
Materias.remove(depBorrar)
print(i)
