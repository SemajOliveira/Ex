from math import hypot
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

print(f'Os valores tem o comprimento da hipootenusa de {hypot(co, ca):.2f}')
