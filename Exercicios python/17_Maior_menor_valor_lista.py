lista = []
maior = 0
menor = 0
for n in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {n}: ')))
    if n == 0:
        maior = lista[n]
        menor = lista[n]
    else:
        if lista[n] > maior:
            maior = lista[n]
        if lista[n] < menor:
            menor = lista[n]

print(f'Você digitou os valores = {lista}')
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for p, q in enumerate(lista):
    if q == menor:
        print(f"{p}...", end='')
print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for p, q in enumerate(lista):
    if q == maior:
        print(f'{p}...',end='')
