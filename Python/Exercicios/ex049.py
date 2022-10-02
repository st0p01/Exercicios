from time import sleep
valor = int(input('Digite um valor: '))

print('Carregando...')
sleep(2)
for x in range(1, 11):
   sleep(1)
   print(f'7 x {x} = {x * valor}')
