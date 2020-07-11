import random
print('<->'*20)
print('Vamos jogar par ou impar?')
print('<->'*20)
count1 = 0
count2 = 0
while True:
    m = random.randint(0, 10)
    n = int(input('Digite um valor: '))
    s = n + m
    esc = ' '
    while esc not in 'PI':
        esc = str(input('Par ou impar? [P/I] ')).strip().upper()
    if s % 2 == 0:
        tot = s
        s = 'par'
        if esc in 'Pp':
            count1 += 1
            print(f'Você jogou {n} e o  computador {m}. Total deu {tot} que é {s}')#Você ganhou
        else:
            print(f'Você jogou {n} e o  computador {m}. Total deu {tot} que é {s}')#Você perdeu
            break
    elif s % 2 != 0:
        tot = s
        s = 'impar'
        if esc in 'Ii':
            count2 += 1
            print(f'Você jogou {n} e o  computador {m}. Total deu {tot} que é {s}')#Você ganhou
        else:
            print(f'Você jogou {n} e o  computador {m}. Total deu {tot} que é {s}')#Você perdeu
            break
    print('Você VENCEU! \nVamos jogar novamente...')
print('-'*20)
print(f'Game Over! Você venceu {count1 + count2} vezes')
print('-'*20)

