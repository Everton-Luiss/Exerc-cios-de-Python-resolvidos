import random
print('Olá, sou seu computador. Pensei num número de 0 a 10. Você consegue adivinhar?')
p = int(input('Qual o seu palpite: '))
num = random.randint(0,10)
count = 0
while p != num:
    if p > num:
        p = int(input('Menos... tente outra vez: '))
    elif p < num:
        p = int(input('Mais... Tente outra vez: '))
    count += 1
print('Você acertou com {} tentativas. Parabéns!'.format(count + 1))
