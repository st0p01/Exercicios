peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura * altura) 
if imc < 18.5:
   print(f'O IMC dessa pessoa é igual a {imc:.1f} \nVocê está ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
   print(f'O IMC dessa pessoa é igual a {imc:.1f} \n PÁRABENS, você está faixa de PESO NORMAL')
elif 25 <= imc < 30:
   print(f'O IMC dessa pessoa é igual a {imc:.1f} \n ')
elif 30 <= imc < 40:
   print(f'O IMC dessa pessoa é igual a {imc:.1f} \n')
else:
   print(f'O IMC dessa pessoa é igual a {imc:.1f} \nVocê está em OBESIDADE MÓRBIDA, cuidado!')
