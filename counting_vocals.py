palabra = input("Ingresa una palabra y sabras cuantas vocales tiene: ")
vocales = 0
for x in palabra:
    y = x.lower()
    vocales += 1 if y == 'a' or y == 'e' or y == 'i' or y == 'o' or y =='u' else 0
print(palabra, " tiene un total de ",vocales, " vocales")
