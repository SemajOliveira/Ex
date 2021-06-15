print('\033[32mAluguel de carro\033[m\n')
km = float(input('Digite a quantidade de Km rodados: '))
dias = int(input('Digite a quantidade de dias:  '))
tot = (km * 0.15) + (dias * 60)
print(f'Ao todo você pagará R${tot:.2f}')

