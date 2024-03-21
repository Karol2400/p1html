def Convertir_Temperatura(C):
    fahrenheit=(C*1.8)+32
    return fahrenheit

TemperaturaCentigrados=float(input("¿Cuál es el valor de su temperatura en grados centigrados? "))
fahrenheit=Convertir_Temperatura(TemperaturaCentigrados)
print(f'El valor de los grados en fahrenheit es {fahrenheit}')