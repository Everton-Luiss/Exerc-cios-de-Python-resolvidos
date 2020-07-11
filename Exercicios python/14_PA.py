a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
q = int(input('Quantos termos vocÊ gostaria de imprimir? '))
print('Os 10 primeiros termos da PA são: ')
n = -1
while n < q - 1:
    n += 1
    an = a1 + n*r
    print('{}'.format(an), end=' -> ')
print('FIM')

