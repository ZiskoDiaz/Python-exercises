def esMayor(usuario):
    return usuario.edad > 17
class Usuario:
    def __init__(self,edad):
        self.edad = edad
# iniciamos el objeto
usuario = Usuario(15)
usuario2 = Usuario(21)

resultado1 = esMayor(usuario)
resultado2 = esMayor(usuario2)

print(resultado1, resultado2)
