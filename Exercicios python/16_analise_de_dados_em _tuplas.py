tupla = (int(input('Digite um  número: ')),
int(input('igite outro número: ')),
int(input('Digite mais um número: ')),
int(input('Digite o último número: ')))
print(f'O número 9 aparece {tupla.count(9)} vezes.')
if 3 in tupla:
    print(f'O número 3 aparece na posição {tupla.index(3) + 1}')
else:
    print('O valor 3 não foi digitado.')
count = 0
for n in tupla:
    if n % 2 == 0:
        count += 1
print(f'Apareceram {count} números pares.')
print(tupla)
