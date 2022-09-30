n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1 + n2)/2

print(f'A sua média foi {n:.1f}')

if n >= 6.0:
   print('Sua média foi boa! PARABENS')
else:
   print('Sua média foi ruim, estude mais!')
