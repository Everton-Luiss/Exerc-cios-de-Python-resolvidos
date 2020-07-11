n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2)/2
if 5 <= media < 7:
    print('O aluno está em recuperação')
elif media > 7:
    print('O aluno está aprovado: ')
else:
    print('O aluno está reprovado')
