def agregaNombreAlArchivo(nombre, apellido):
    c = open('nombre_completo.txt', 'a')
    c.write (nombre + " " + apellido + " \n")
    c.close()
agregaNombreAlArchivo("Francisco", "Diaz")
