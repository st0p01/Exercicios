i = '=' * 20
print(f'{i} Loja ST0P01 {i}')
preço = float(input('Preço das comprar R$: '))
print('''FORMAS DE PAGAMENTO
 [ 1 ] á vista dinheiro/cheque
 [ 2 ] á vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')

opção = int(input('Qual é a sua opção? '))
if opção == 1:
   c = preço - (preço * 10 / 100)
elif opção == 2:
   c = preço - (preço * 5 / 100)
elif opção == 3:
   c = preço
   parcela = c3 / 2
   print(f'Sua compra será parcelada em 2x de {parcela:.2f}')
elif opção == 4:
   c = preço + (preço * 20 / 100)
   tp = int(input('Quantas parcelas?'))
   parcela = preço / tp
   print(f'Sua compra será parcelada em {tp}x de R${parcela:.2f} COM JUROS')
else:
   c = preço
   print('Opção INVALIDA, tente novamente mais tarde...')
print(f'A sua compra de R${preço:.2f} vai custar R${c:.2f} no final')
