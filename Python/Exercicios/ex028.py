from random import randint
print('--='*22)
print('Vou pensar em um número entre 0 e 5 , tente adivinhar')
print('--='*22)

n = randint(0, 5)
r = int(input('Em que número eu pensei: '))
print('Processando...')

if r == n:
   print('PARABÉS!! você conseguiu me vencer!')
else:
   print(f'GANHEI!! Eu pensei no número {n} e não no número {r}')
