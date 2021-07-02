cantidad_invertir = int(input("ingresa cantidad invertir: "))
interes_anual = int(input("ingresa interes anual: "))
num_years = int(input("ingresa cantidad de anhos: "))

capital = (cantidad_invertir+((cantidad_invertir*interes_anual)/100))*num_years

print ("el resultado de ", cantidad_invertir, " con interes anual de ", interes_anual, "% en la cantidad de ", num_years, " le generara una gananacia de ", capital)
