r = 0
cont = 0
for x in range(1, 501 , 2):
   if x % 3 == 0:
      r += x
      cont += 1
print(f'A soma entre os {cont} valores solicitados é {r}')