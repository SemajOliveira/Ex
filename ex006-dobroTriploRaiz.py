#from math import sqrt
n = int(input('Digite um valor: '))
r = n ** (1/2) #raiz sem precisar da biblioteca também poderia ser print(pow(n, (1/2)))
print(f'O dobro de {n} é {n*2}')
print(f'O triplo de {n} é {n*3}')
#print(f'A raiz de {n} é {sqrt(n):.2f}')
print(f'A raiz de {n} é {r:.2f}')
