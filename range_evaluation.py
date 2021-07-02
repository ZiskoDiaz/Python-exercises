evaluacion = float(input("ingrese su evaluacion, recuerde debe ser 0.0 - 0.4 - 0.6 " ))
if evaluacion == 0.0 or evaluacion == 0.4 or evaluacion == 0.6:
    bono = evaluacion * 100000
    print ("Su evaluacion fue " ,evaluacion, " y su bono sera de ",bono,  "pesos.")

else:
    print ("Dato error")
