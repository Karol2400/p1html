class perro:
    def __init__(self, nombre, raza):
        self.nombre=nombre
        self.raza=raza
    def ladrar (self):
        print("gau gau ")
        #Dos maneras de imprimir
        print(f'hola {self.nombre}')
        print("hola", self.nombre)
perro1=perro("loquis", "doberman")
perro1.ladrar()

perro2=perro("Max", "Salchicha")