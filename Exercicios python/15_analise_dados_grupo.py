count = 0
count2 = 0
count3 = 0
while True:
    print('-'*20)
    print('Cadastre uma pessoa.')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()#Aqui pode começar o sexo como vazio
    while sexo not in 'MF':
        sexo = str(input('Por favor, digite M ou F: ')).strip().upper()
    if idade > 18: # É importante colocar esses dois ifs antes do break
        count += 1
    if sexo in 'M':
        count2 += 1
    if sexo in 'F' and idade < 20:
        count3 += 1
    c = str(input('Quer continuar? [S/N] ')).strip().upper()
    while c not in 'SN':
        c = str(input('Entrada inválida. Digite S ou N: ')).strip().upper()
    if c == 'N':
        break
print(f'O total de pessoas com mais de 18 anos é: {count}')
print(f'Ao todo temos {count2} homens cadastrados')
print(f'Temos {count3} mulheres com menos de 20 anos')