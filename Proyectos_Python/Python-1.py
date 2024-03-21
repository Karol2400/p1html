nombre="Karol"
frase1="A las personas que no les gusta conducir nunca aprenden a derrapar"
Frase2="El pasado no puede cambiarse, pero el futuro siempre esta abierto a posibilidades"
frase3="A veces el unico modo de superarlo es repasar las cosas de tu pasado que no te dejan seguir adelante... tienes que lidiar con eso, no que tan temible sea, porque cuando lo hagas veras que avanzado mas de lo que nunca imaginaste posible"

print(nombre)
print(nombre[4])
print(nombre[1:3])

print(frase1[12])

primerpalabra=frase1.split()
print(primerpalabra[3])

#Mayusculas
print(nombre.upper())
#Minusculas
print(nombre.lower())
#Tipo de variable
print(type(nombre))
cadenita="TenGO YHaMBre"
print(cadenita.swapcase())
cad="apuesto que si es apuesto porque por supuesto es mas apuesto que yo"
print(cad.count("puesto"))