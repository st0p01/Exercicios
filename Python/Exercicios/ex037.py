numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para a conversão: \n [1] converter para BINÁRIO \n [2] converter para OCTAL \n [3] converter para HEXADECIMAL')

o = int(input('Sua opção: '))

if o == 1:
   print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}')
elif o == 2:
   print(f'{numero} convertido para OCTAL é igual a {oct(numero)[2:]}')
elif o == 3:
   print(f'{numero} covertido para HEXADECIMAL é igual a {hex(numero)[2:]}')
else:
   print('Opção invalida, tente novamente')