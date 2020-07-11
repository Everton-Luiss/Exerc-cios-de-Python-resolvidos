c = str(input('Vamos começar? [S/N]: ')).strip().upper()
lista = []
count = 0
while c not in 'Nn':
    n = int(input('Digite um número: '))
    count += 1
    c = str(input('Quer continuar? [S/N]: ' )).strip().upper()
    lista.append(n)
    lista.sort()
#print(lista)
m = sum(lista)/len(lista)
print(sum(lista))
print('Você digitou {} números e a média foi {}'.format(count, m))
print('O maior valor foi {} e o menor valor foi {}'.format(lista[0], lista[count-1]))
print('Até a próxima!!!')
