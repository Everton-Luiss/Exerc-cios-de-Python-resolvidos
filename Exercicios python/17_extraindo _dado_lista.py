lista = []
count = 0
while True:
    n = int(input('Digite um valor: '))
    count += 1
    op = str(input('Quer continuar? [S/N]: ')).strip().upper()
    lista.append(n)
    while op not in 'SN':
        op = str(input('Entrada inválida. Por favor digite S ou N: ')).strip().upper()
        if op == "N":
            break
        if op == 'S':
            print()
    if op == 'N':
        break
lista.sort(reverse=True)
if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontrado na lista!')
print(f'Você digitou {count} valores.')
print(f'Os valores em ordem decrescente são {lista}')
