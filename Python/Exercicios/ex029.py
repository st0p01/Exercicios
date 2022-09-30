velocidade = int(input('Qual é a velocidade atual do carro? '))

if velocidade > 80:
    m = (velocidade - 80) * 7 
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h') 

    print(f'Você deve pagar um multa de {m:.2f}!') 
   
print('Tenha um bom dia! Dirija com segurança')