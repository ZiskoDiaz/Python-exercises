c = open('document.txt', 'a')

c.write("\n  Agregamos esta linea nueva a nuestro archivo")

c.close() # asi cerramos el archivo

x = open('document.txt')

print(x.read())
