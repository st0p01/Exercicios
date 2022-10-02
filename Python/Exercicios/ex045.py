from random import randint
import time

itens = ('Pedra', 'Papel', 'Tesoura')
print('''Suas opções:
 [0] Pedra
 [1] Papel
 [2] Tesoura''')
pc = randint(0,2)
player = int(input('Sua escolha: '))

print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ!!')

print(20*'-=')
print('O jogador escolheu {}'.format(itens[player]))
print('O computador escolheu {}'.format(itens[pc]))
print(20*'-=')

if pc == 0 :
   if player == 0:
      print('\033[33mEMPATE\033[m')
   elif player == 2:
      print('O jogador \033[31mPERDEU\033[m')
   else:
      print('O jogador \033[32mVENCEU\033[m')
elif pc == 1:
   if player == 1:
      print('\033[33mEMPATE\033')
   elif player == 0:
      print('O jogador \033[31mPERDEU\033[m')
   else:
      print('O jogador \033[32mVENCEU\033[m')
else:
   if player == 2:
      print('\033[33mEMPATE\033')
   elif player == 1:
      print('O jogador \033[31mPERDEU\033[m')
   else:
      print('O jogador \033[32mVENCEU\033[m')

   