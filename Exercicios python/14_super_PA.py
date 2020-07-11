a1 = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razão da PA: '))
q = int(input('Quantos termos você gostaria de mostrar? '))
n = -1
count = 0
while n < q - 1:
    n += 1
    an = a1 + n*r
    count += 1
    #print(n)
    print('{}'.format(an), end=' -> ')
print('Pausa')
m = int(input('Quantos termos você que mostrar a mais? '))
while m != 0:
    count2 = 0
    p = n
    while p < n + m:
        p += 1
        an = a1 + p*r
        count2 += 1
        print('{}'.format(an), end=' -> ')
    print('Pausa')
    m = int(input('\nQuantos termos você que mostrar a mais? '))
    n = p
print('Progressão finalizada com {} termos motrados.'.format(count + count2))
