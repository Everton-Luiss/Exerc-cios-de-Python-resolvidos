sexo = str(input('Digite seu sexo: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Entrada inválida! Digite M ou F: ')).strip().upper()
print('Sexo {} registrado com sucesso!'.format(sexo))