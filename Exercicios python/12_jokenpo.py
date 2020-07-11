import random
import time
print('''Suas opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
opcao = int(input('Sua opção: '))
computador = random.randint(1,3)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!!')
print('<=>'*20)
print('''Computador jogou {} 
Jogador jogou {}'''.format(computador, opcao))
print('<=>'*20)
if computador == 1:
    if opcao ==1:
        print('Empate')
    elif opcao == 2:
        print('Jogador ganha!')
    elif opcao == 3:
        print('Computador ganha!')
    else:
        print('Opcao invalida')
elif computador == 2:
    if opcao == 1:
        print('Computador ganha!')
    elif opcao == 2:
        print('Empate!')
    elif opcao == 3:
        print('Jogador ganha!')
    else:
        print('Opcao invalida')
elif computador == 3:
    if opcao == 1:
        print('Jogador ganha')
    elif opcao == 2:
        print('Coputador ganhar')
    elif opcao == 3:
        print('Empate')
    else:
        print('Opcao invalida')



