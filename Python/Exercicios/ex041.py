from datetime import date
idade= int(input('Ano que nasceu: '))
ano = date.today().year
resultado = ano - idade

if resultado <= 9:
   print(f'O atleta tem {resultado} anos \nClassificação: MIRIM')
elif resultado <= 14:
   print(f'O atleta tem {resultado} anos \nClassificação: INFANTIL')
elif resultado <= 19:
   print(f'O atleta tem {resultado} anos \nClassificação: JUNIOR')
elif resultado <= 25:
   print(f'O atleta tem {resultado} anos \nClassificação: SENIOR')
else:
   print(f'O atleta tem {resultado} anos \nClassificação: MASTER')
