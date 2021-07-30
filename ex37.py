n = int(input('Digite um valor: '))
print("""Escolha a base de conversão: 
1- Binário
2- Octal
3- Hexadecimal""")
base = int(input('Item escolhdo: '))

if base == 1:
    print(f'{n} em binário é: {bin(n)[2:]}')
elif base == 2:
    print(f'{n} em octal é: {oct(n)[2:]}')
elif base == 3:
    print(f'{n} em hexadecimal é: {hex(n)[2:]}')
else:
    print('Valor Inválido')
