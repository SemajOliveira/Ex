vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    multa = 7 * (vel - 80)
    print(f'Velocidade exceida, Multa de {multa}R$ aplicada')
    print('Dirija com mais cuidado')
else:
    print('Continue Dirigindo Com Cuidado. Boa Viagem!')
