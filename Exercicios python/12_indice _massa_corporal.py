peso = float(input('Digite o seu peso:'))
altura = float(input('Digite sua altura: '))
IMC = peso/(altura*altura)
print('Seu IMC é {} '.format(IMC))
if IMC < 18.5:
    print('Abaixo do peso')
elif 18.5 <= IMC < 25:
    print('Peso ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Obesidade morbida')