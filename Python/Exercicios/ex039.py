from datetime import date
ano = int(input('Ano de nascimento: '))
atual = date.today().year
idade = 2017 - ano 

if idade == 18:
   print(f'Você tem que se alistar IMEDIATAMENTE')

elif idade < 18:
   faltam = 18 - idade
   print(f'Ainda faltam {faltam} anos para o alistamento')
else:
   faltaram = idade - 18
   print(f'Você já deveria ter se alistado há {faltaram} anos')