import time
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''[ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR''')
    opcao = int(input('Qual a sua opção: '))
    if opcao == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}: '.format(n1 , n2, s))
    elif opcao == 2:
        m = n1*n2
        print('O produto entre {} e {} é {}: '.format(n1, n2, m))
    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior número é {}: '.format(n1, n2, n1))
        elif n1 < n2:
            print('Entre {} e {} o mair número é {}: '.format(n1, n2, n2))
        else:
            print('Os números são iguais.')
    elif opcao == 4:
        print('Informe novos números. ')
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Opção inválida! Tente novamente.')
print('FIM DO PROGRAMA')