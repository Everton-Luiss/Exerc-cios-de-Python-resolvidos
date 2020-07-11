from datetime import date
ano = int(input('Qual o seu ano de nascimento?'))
idade = date.today().year - ano
if idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - idade))
elif idade > 18:
    print('Você deveria ter se alistado {} anos atrás'.format(idade -18))
else:
    print('Corre lá e vá se alistar.')