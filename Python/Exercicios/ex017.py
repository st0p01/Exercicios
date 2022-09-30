import math


import math
cp = float(input('Comprimento do cateto oposto: '))
cd = float(input('Comprimento do cateto adjacente: '))
r1 = math.hypot(cp, cd)
print(f'A hipotenusa vai medir {r1:.2f}')