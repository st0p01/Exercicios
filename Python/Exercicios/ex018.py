import math
v = int(input('Digite o ângulo que você deseja: '))
c = math.cos(math.radians(v))
t = math.tan(math.radians(v))
s = math.sin(math.radians(v))
print(f'O ângulo de {v:.2f} tem o SENO de {s:.2f}')
print(f'O ângulo de {v:.2f} tem o COSSENO de {c:.2f}')
print(f'O ângulo de {v:.2f} tem o TANJENTE de {t:.2f}')