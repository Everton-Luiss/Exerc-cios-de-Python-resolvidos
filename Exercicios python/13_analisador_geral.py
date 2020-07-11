lidade = []
count = 0
maior = 0
anomevelho = ''
for n in range(1, 5):
    print('--------{}ª PESSOA-----------'.format(n))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: '))
    lidade.append(idade)
    if n == 1 and sexo in 'Mm':
        maior = idade
        nomevelho = nome
    if idade > maior:
        maior = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        count += 1
m = sum(lidade)/len(lidade)
print('A idade média do grupo é: {}'.format(m))
print('O homem mais velho tem {} anos e se chama {}'.format(idade, nome))
print('Ao todo são {} mulheres com menos de 20 anos'.format(count))
print(lidade)

