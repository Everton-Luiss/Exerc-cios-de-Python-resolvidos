s = count = 0
while True:
    n = int(input('Digite um número(999 para parar): '))
    count += 1
    if n == 999:
        break
    s += n
print(f'Você digitou {count - 1}  números e a soma foi de {s}')
print('FIM')