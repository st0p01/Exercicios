nota = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

resultado = (nota + nota2) / 2

if resultado < 5.0:
   print(f'Tirando {nota} e {nota2}, a média do aluno é {resultado}\nO aluno está REPROVADO')
elif resultado > 6.9:
   print(f'Tirando {nota} e {nota2}, a média do aluno é {resultado}\nO aluno PASSOU')
else :
   print(f'O Tirando {nota} e {nota2}, a média do aluno é {resultado}\nO aluno está de RECUPERAÇÃO')