lista = []
print ("Ingresa un valor, para salir solo di BASTA")
while True:
    valor = input('ingrese valor: ')
    if valor == "basta":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print('dato invalido')
            exit()
resultado = 0
for x in lista:
    resultado += x
print(resultado)
