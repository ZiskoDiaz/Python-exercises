# creador de clases
class Usuario:
    # metodos
    def __init__(self, nombre, apellido, edad):
        # instanciamos
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# generamos una instancia
usuario = Usuario("Francisco", "Diaz", 29) #llamamos a la clase de usuario

print (usuario.nombre , usuario.apellido , usuario.edad)
