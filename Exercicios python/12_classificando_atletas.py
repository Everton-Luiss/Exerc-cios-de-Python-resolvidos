from datetime import date
ano = int(input('Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print('Clasificação mirim')
elif idade <= 14:
    print('Classificação infantil')
elif idade <= 19:
    print('Classificação Júnior')
elif idade <=25:
    print('Classificação Sênior')
else:
    print('Classificação Master')