from random import choice
print('Entre com os nomes dos alunos')
n1 = input('Aluno1: ')
n2 = input('Aluno2: ')
n3 = input('Aluno3: ')
n4 = input('Aluno4: ')
sorteio = [n1, n2, n3, n4]
print(f'\n{choice(sorteio)} apagará o quadro')
