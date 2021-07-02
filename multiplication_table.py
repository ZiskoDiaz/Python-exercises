tabla = int(input("indique tabla de multiplicar : "))
i = 1
total = tabla
for i in range( 0, 10):
    i = i + 1
    total = tabla * i
    print ( i, "x", tabla, " = ", total)
