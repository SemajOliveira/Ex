sal = float(input('Digite seu salário: '))
if sal > 1250:
    aumento10 = sal + (sal * 10/100)
    print(f'Seu novo salário com aumento de 10% será de R${aumento10}')
elif sal <= 1250:
    aumento15 = sal + (sal * 15/100)
    print(f'Seu novo salário com aumento de 15% será de R${aumento15}')
