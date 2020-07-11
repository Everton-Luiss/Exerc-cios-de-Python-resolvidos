lista = []
count = 0
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = str(input('Quer continuar? [S/N] ')).strip().upper()
    while op not in "SN":
        op = str(input('Por favor, digite S ou N: ')).strip().upper()
        if op in 'N':
            break
        if op in 'S':
            print()
    if op in 'N':
        break
lista.sort()
print(f'Você digitou os valores {lista}')
print('FIM')

