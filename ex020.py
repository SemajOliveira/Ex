from random import shuffle
print('Entre com os nomes dos alunos')
n1 = input('Aluno1: ')
n2 = input('Aluno2: ')
n3 = input('Aluno3: ')
n4 = input('Aluno4: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print(f'\nA ordem de apresentação é: {lista}')
