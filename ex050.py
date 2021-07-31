s = 0
for numeros in range(1, 7):
    valor = int(input(f'Digite o Valor{numeros}: '))
    if valor % 2 == 0:
        s += valor
print(f'A soma dos Pares é: {s}')
