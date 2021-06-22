a = float(input('Digite o valor da 1ª reta: '))
b = float(input('Digite o valor da 2ª reta: '))
c = float(input('Digite o valor da 3ª reta: '))

if a < b + c and b < c + a and c < b + a:
    print('As retas digitadas PODEM formar um triângulo!')
else:
    print('As retas digitadas NÃO PODEM formar um triângulo!')