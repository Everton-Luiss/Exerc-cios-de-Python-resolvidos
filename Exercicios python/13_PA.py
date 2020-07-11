p = int(input('Digite o primeiro termo da P.A: '))
r = int(input('Digite a razão da P.A: '))
for n in range(1,11):
    an = p + (n-1)*r
    print(an, end=' -> ')
print('FIM')