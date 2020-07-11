lista = []
for n in range(1, 6):
    peso = float(input('Digite o peso da {} pessoa: '.format(n)))
    lista.append(peso)
    lista.sort()
print(lista)
print('O maior e o menor peso lido foram respectivamente {}kg e {}kg'.format(lista[4], lista[0]))