salario = int(input('Qual é o salário do funcionario?'))

if salario <= 1250:
   aumento = salario + (salario * 15 / 100)
   print(f'Quem ganhava R${salario:.2f} passa a ganhar R${aumento:.2f} agora')
else:
   aumento = salario + (salario * 10 / 100)
   print(f'Quem ganhava R${salario:.2f}passa a ganhar {aumento:.2f}')