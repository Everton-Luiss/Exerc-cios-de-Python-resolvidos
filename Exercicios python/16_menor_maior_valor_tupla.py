import random
num = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10),
       random.randint(1,10))
print('Os valores sorteados foram: ', end=' ')
for n in num:
    print(f'{n}', end=' ')
p = sorted(num)
print(f'\nO menor e o maior valor são respectivamente {p[0]} e {p[4]}.')