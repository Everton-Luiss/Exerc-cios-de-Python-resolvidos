num = int(input('Digite um número: '))
print('O resto da divisão é: :  ')
lista = []
for n in range(1,num+1):
    r = num % n
    if r == 0:
        print('\033[32m{}\033[m'.format(r), end=' ')
    else:
        print('\033[31m{}\033[m'.format(r), end = ' ')
    lista.append(r)
#print(lista)
if lista.count(0) == 2:
        print('\nO resto da divisão foi zero {} vezes. Portanto este número é primo.'.format(lista.count(0)))
else:
        print('\nO resto da divisão foi zero {} vezes. Portanto este número não é primo.'.format(lista.count(0)))

