barato = s = cont = 0
while True:
    nome = input('Nome do produto:> ')
    preco = float(input('Digite o preço do produto: '))
    op = input('Você deseja continuar? [Sim/ Não] ').strip().lower()[0]
    s += preco
    if preco < 1000:
        cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome    
    if op == 'n':
        break

print(f'Ao todo seus produtos iram custar R$ {s}')
print(f'{cont} produtos custam menos que R$ 1000')
print(f'O produto mais barato é o {barato}')
