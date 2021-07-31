from time import sleep
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um mesmo/outro valor: '))
while True:
    print("""Menu de opções
    1- Somar
    2 - Multiplicar
    3 - Maior
    4- Novos números
    5- Sair do programa""")
    opc = int(input('Qual opção você esolhe[Número]: '))
    if opc == 1:
        print(f'{n1} + {n2} = {n1 + n2}\n')
        print('\033[36m---\033[m'*20)
        sleep(1)
    elif opc == 2:
        print(f'{n1} X {n2} = {n1 * n2}')
        print('\033[36m---\033[m'*20)
        sleep(1)
    elif opc == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            print('\033[36m---\033[m'*20)
            sleep(1)
        else:
            print(f'{n2} é maior que {n1}')
            print('\033[36m---\033[m'*20)
            sleep(1)
    elif opc == 4:
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite um mesmo/outro valor: '))
    elif opc == 5:
        print(f'Programa Encerrado...')
        break
    else:
        print('Opção inválida, tente novamente')
