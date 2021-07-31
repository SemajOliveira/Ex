nota1 = float(input('Digite a nota1: '))
nota2 = float(input('Digite a nota2: '))
média = (nota1+nota2) / 2

if média < 5.0:
    print('REPROVADO!')
elif média > 5.0 and média < 6.9:
    print('RECUPERAÇÃO!')
elif média > 7.0:
    print('Aprovado')