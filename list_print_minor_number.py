lista = [1,3,5,7,9,-2,-4,-6,-8,100,200,-24,-13]
menor = 'init'
for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor
print('De la lista', lista, 'el numero menor es: ', menor)
