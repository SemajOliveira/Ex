print('Digite quatro valores')
n1 = int(input('1º valor: '))
n2 = int(input('2º valor: '))
n3 = int(input('3º valor: '))
n4 = int(input('4º valor: '))
tupla = (n1, n2, n3, n4)
print('-----'*20)
print(f'O número 9 apareceu {tupla.count(9)} vezes')
try:
    print(f'O primeiro nº 3 apareceu na posição: {tupla.index(3)+1}')
except ValueError:
    print('3 Não foi digitado')
print('Os número pares são: ', end=' ')
for j in tupla:
    if j != 0:
        if j % 2 == 0:
            print(j, end='| ')
