menor_preco = 0
nome_barato = ''
count0 = 0
count1 = 0
s = 0
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    s += preco
    count0 += 1
    if preco > 1000:
        count1 += 1
    if count0 == 1:   #Dá pra simplificar colocando aqui if count0 == 1 or preco < menor_preco: e apagando o else
        menor_preco = preco
        nome_barato = nome
    else:
        if preco < menor_preco:
            menor_preco = preco
            nome_barato = nome
    resp = str(input('Quer continuar [S/N]: ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Entrada inválida. Digite S ou N: ')).strip().upper()
    if resp in 'N':
        break
print(f'O total da compra foi: {s}')
print(f'Temos {count1} produtos custando mais de R$1000')
print(f'O produto mais barato foi a {nome_barato} que custa {menor_preco}')