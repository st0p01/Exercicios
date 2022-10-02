resultado = 0
cont = 0
for x in range(0, 6):
   número = int(input('Digite um número: '))
   if número % 2 == 0:
      resultado += número
      cont += 1
print(f'Você iformou {cont} números PARES e a soma foi {resultado}')
