class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    def saludo(self):
        print("Hola, soy un ", self.tipo, " y mi sonido es", self.onomatopeya)


class Gato(Animal):
    tipo = "gato"
    def __init__(self, nombre, onomatopeya): #extendiendo con self
        Animal.__init__(self, nombre, onomatopeya)
        print(" GATO EN EXTENSIOOOOON")

class Perro(Animal):
    tipo = "perro"
    def __init__(self, nombre, onomatopeya): #extendiendo con super
        super().__init__(nombre, onomatopeya)
        print(" PERRO EXTENDIDOOOO")

class Vaca(Animal):
    tipo = "vaca"

gato = Gato("Misifus", "Maullido")
gato.saludo()

perro = Perro("Cafe", "Ladrido")
perro.saludo()

vaca = Vaca("Lola", "Mugido")
vaca.saludo()
