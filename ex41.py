from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
if idade <= 9:
    print('MIRIM')
elif idade >= 9 and idade <= 14:
    print('INFANTIL')
elif idade >= 14 and idade <= 20:
    print('SẼNIOR')
else:
    print('MASTER')
