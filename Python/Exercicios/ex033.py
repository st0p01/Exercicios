from re import A


v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))

menor = v1 
if v2 < v1 and v2 < v3:
   menor = v2
if v3 < v1 and v3 < v2:
   menor = v3

maior = v1
if v2 > v1 and v2 > v3:
   maior = v2
if v3 > v1 and v3 > v2:
   maior = v2
print(f'O menor valor digitado foi {menor}')
print(f'E o maior número digitado foi {maior}')