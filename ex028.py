from random import randint
pc = randint(0, 5)

print('\033[1;30;46m Tente Descobrir em qual número eu estou pensando\033[m')
value = int(input('Digite um valor:> '))
if pc == value:
    print(f'\033[32mAcertou, pensei mesmo no número {value}\033[m')
elif pc != value:
    print(f'\033[31mVocê errou, pensei no número {pc}\033[m')
