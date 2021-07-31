from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('''Suas opções: 
\n[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\n''')

jogador = int(input('Qual a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)

print('-=' * 13)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('=-' *13)

if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('Jogada Inválida!')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('Opção Inválida!')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('Opção inválida!')