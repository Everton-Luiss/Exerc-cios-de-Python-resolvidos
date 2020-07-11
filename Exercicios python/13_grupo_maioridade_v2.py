from datetime import  date
atual = date.today().year
lista = []
count = 0
for n in range(1,8):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(n)))
    idade = atual - ano
    lista.append(idade)
    if idade >= 18:
        count += 1
#print(lista)
#print(count)
print('Ao todo tivemos {} pessoas maiores de idade e {} pessoas menores de idade'.format(count, 7 - count))
