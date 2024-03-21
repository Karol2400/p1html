Nombre=input("¿Cuál es su nombre? ")
print("")
print("dd/m/a")
print("")
Fecha=(input("¿Cual es su fecha de nacimiento? "))
print("")
Fechita=Fecha.split("/")
print(Fechita)
print("")
Dia=int(Fechita[0])
print(Dia)
print("")
Mes=int(Fechita[1])
print(Mes)
print("")
if(Mes==1 and Dia<=19) or (Mes==2 and Dia<=15):
    print("Eres un Capricornio")
    print("")
elif(Mes==2 and Dia<=16) or (Mes==3 and Dia<=11):
    print("Eres un Acuario")
    print("")
elif(Mes==3 and Dia<=12) or (Mes==4 and Dia<=18):
    print("Eres un Piscis")
    print("")
elif(Mes==4 and Dia<=19) or (Mes==5 and Dia<=13):
    print("Eres un Aries")
    print("")
elif(Mes==5 and Dia<=13) or (Mes==6 and Dia<=19):
    print("Eres un Tauro")
    print("")
elif(Mes==6 and Dia<=20) or (Mes==7 and Dia<=20):
    print("Eres un Geminis")
    print("")
elif(Mes==7 and Dia<=21) or (Mes==8 and Dia<=9):
    print("Eres un Cancer")
    print("")
elif(Mes==8 and Dia<=10) or (Mes==9 and Dia<=15):
    print("Eres un Leo")
    print("")
elif(Mes==9 and Dia<=16) or (Mes==10 and Dia<=30):
    print("Eres un Virgo")
    print("")
elif(Mes==10 and Dia<=31) or (Mes==11 and Dia<=22):
    print("Eres un Libra")
    print("")
elif(Mes==11 and Dia<=23) or (Mes==11 and Dia<=29):
    print("Eres un Escorpio")
    print("")
elif(Mes==11 and Dia<=30) or (Mes==12 and Dia<=17):
    print("Eres un Ofiuco")
    print("")
elif(Mes==12 and Dia<=18) or (Mes==1 and Dia<=18):
    print("Eres un Ofiuco")
    print("")