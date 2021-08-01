while True:
    n = int(input('Qual tabuada você quer ver? '))
    if n < 0:
        print('Programa Encerrado...')
        break
    else:
        for i in range(1, 11):
            print(f'{n} X {i} = {n * i}')
        print('\033[32m---\033[m'*20)

