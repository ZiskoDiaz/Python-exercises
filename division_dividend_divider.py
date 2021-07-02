dividendo = int(input("ingresar el valor de dividendo: "))
divisor = int(input("ingresar el valor de divisor: "))
while divisor == 0:
    print ("ERROR: no se puede dividir por 0")
    divisor = int(input("ingresar el valor de divisor: "))

resultado = dividendo / divisor

print ("el resultado es", resultado)
