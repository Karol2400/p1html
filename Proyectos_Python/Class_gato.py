class gato:
    def __init__(self, nombre , colorpelaje, peso, raza, tamaño):
        self.nombre=nombre
        self.colorpelaje=colorpelaje
        self.peso=peso
        self.raza=raza
        self.tamaño=tamaño
    def maullar (self):
        print("miau miau ")
    def slatar(self):
        print("Salta")
    def dormir (self):
        print("zzz")
    def defecar (self):
        print("...")
    def comer (self):
        print("Esta comiendo")
gato1=gato("Loquis", "Blanco", "10 kg", "Siames", "30 cm")
gato1.maullar()
gato1.slatar()
gato1.comer()
gato1.defecar()