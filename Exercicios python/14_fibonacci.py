n = int(input('Quantos termos você uer mostrar: '))
c = -1
s = 0
while c < 1:
    c += 1
    s += c
    print(s, end = ' -> ')
a = 1
b = 0
p = 0
while p < n:
    p = p + 1
    f = a + b
    b = a
    a = f
    print(f, end=' -> ')

