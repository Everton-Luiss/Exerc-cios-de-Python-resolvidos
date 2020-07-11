s = 0
count = 0
for c in range(1,7):
    num =  int(input('Digite um número: '))
    if num % 2 == 0:
        s += num
        count += 1
print('Você informou {} valores pares e soma foi {}'.format(count,s))
print('FIM')