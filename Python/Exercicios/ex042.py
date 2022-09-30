s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s2 + s1:
   print('Os segmento acima PODEM FORMAR um triangulo', end=' ')
   if s1 == s2 == s3:
      print('EQUILÁTERO')
   elif s1 != s2 == s3:
      print('ISÓCELES')
   else:
      print('ESCALENO')
else:
   print('Os segmento acima NÃO PODEM FORMAR um triangulo')