# creador de clases
class Usuario:
    # metodos
    def __init__(self, nombre, apellido, edad):
        # instanciamos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):
        print("Hola, mi nombre es " , self.nombre, self.apellido, "y mi edad es " , self.edad)

# generamos una instancia
usuario = Usuario("Francisco", "Diaz", 29) #llamamos a la clase de usuario

usuario.saludo()
