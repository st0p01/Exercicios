nome = str(input('Qual é o seu nome: '))
if nome == 'Gustavo':
   print('Que nome bonito!')
elif nome in 'Pedro Maria Paulo':
   print('Seu nome é bem popular no brasil')
elif nome in 'Ana Cláudia Jéssica Juliana':
   print('Belo nome feminino')
else:
   print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}!')
