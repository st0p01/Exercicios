distancia = int(input('Qual é a distancia da viagem? '))
print(f'Você está pretes a começar um viagem de {distancia}Km.')

if distancia < 200:
   viagem = distancia * 0.50
   print(f'E o preço da sua passagem será de R${viagem:.2f}')
else:
   viagem = distancia * 0.45
   print(f'E o preço da sua passagem será de R${viagem}')