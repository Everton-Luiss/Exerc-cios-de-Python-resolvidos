a = float(input('Lado a: '))
b = float(input('Lado b: '))
c = float(input('Lado c: '))
if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
    print('Estes lados formam um triângulo ', end='')
    if a == b == c:
        print('Equilátero')
    elif a != b != c != a:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Estes lados não formam um trângulo')