nome = str(input('Digite seu nome: ')).upper().strip()

print('A letra A aparece {} vezes'.format(nome.count('A')))
print('A primeira letra A apareceu na posição {}'.format(nome.find('A')+1))
print('A última letra A apareceu na posição {} '.format(nome.rfind('A')+1))