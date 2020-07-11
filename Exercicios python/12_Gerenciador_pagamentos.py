print('<=>'*20)
print('Lojas Guanabara')
print('<=>'*20)
preco = float(input('Total de compras: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista DINHEIRO/CHEQUE
[ 2 ] à vista CRTÃO
[ 3 ] 2x no CARTÃO
[ 4 ] 3x no CARTÃO
''')
opcao = int(input('Qual a sua opção?: '))
if opcao == 1:
    total = preco - 0.1*preco
elif opcao == 2:
    total = preco - 0.05*preco
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de {}'.format(parcela))
elif opcao == 4:
    total = preco + 0.2*preco
    totalparc = int(input('Quantas parcelas'))
    parcela = total/totalparc
    print('Sua compra será parcelada em {:.2f}x de {:.2f}'.format(totalparc, parcela))
else:
    total = preco
    print('Opção inválida!')
print('Sua compra de {} vai custar {} no final'.format(preco, total))

