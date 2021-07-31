from random import randint
computador = randint(0, 10)
print('\033[31mSou seu computador acabei de pensar em um número entre 0 e 10')
print('Será que você consegue adivinhar qual foi? \033[m')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...Tente mais uma vez')
        elif jogador > computador:
            print('Menos...Tente mais uma vez')
print(f'\033[32mAcertou com {palpite} Tentativas\033[m')
