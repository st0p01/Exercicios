print('='*20)
print('10 TERMOS DE P.A')
print('='*20)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = termo + (10 - 1) * razão

for x in range(termo, décimo + razão, razão):
   print(f'{x} ->', end=" ")
print('ACABOU')