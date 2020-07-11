lista = []
pares = []
impar = []
while True:
    n = int(input('Digite um nímero: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)
    op = str((input('Quer continuar? [S/N]: '))).strip().upper()
    while op not in 'SN':
        op = str((input('Entrada inválida! Digite S ou N: '))).strip().upper()
        if op == 'N':
            break
        if op == 'S':
            print()
    if op == 'N':
        break
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de impares é {impar}')
