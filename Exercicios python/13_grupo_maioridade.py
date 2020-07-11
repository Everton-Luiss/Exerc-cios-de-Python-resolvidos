from datetime import date
from collections import Counter
atual = date.today().year
lista = []
for n in range(1,3):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
    idade = atual - ano
    if idade == 18:
        print('\033[32m\033[m'.format(idade))
    else:
        print('\033[31m\033[m'.format(idade))
    lista.append(idade)
    #if lista.count(18)
print(lista)
c = Counter(lista)
print(c)

Inacabado: preciso encontrar uma maneira de contas o número de ocorrências de um número >= 18 na lista







