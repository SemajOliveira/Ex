num = int(input('Digite um valor inteiro: '))
if num != 0:
    if num % 2 == 0:
        print(f'{num} é PAR')
    else:
        print(f'{num} é ÍMPAR')
else:
    print('Valor Nulo!')
