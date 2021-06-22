km = float(input('DIgite a quantidade de Km percorridos: '))
if km <= 200:
    valorM = km * 0.50
    print(f'Você pagará no final R${valorM} da viagem')
elif km > 200:
    valor = km * 0.45
    print(f'Você pagará no final R${valor} da viagem')

