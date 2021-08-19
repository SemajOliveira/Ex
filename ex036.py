casa = float(input('Valor da casa? '))
salario = float(input('Qual seu salário? '))
anos = float(input('Em quantos anos você vai pagar? '))
prestação = casa / (anos * 12)
mininmo = salario * 30 / 100
print('Paga pagar uma casa de R$ {} em {} anos, a prestação será de R$ {:.2f}'.format(casa, anos, prestação))
if prestação <= mininmo:
    print('Emprestimo pode ser concedidio')
else:
    print('Emprestimo negado')
