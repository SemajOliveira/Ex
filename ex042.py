r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um tirângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero!')
    if r1 != r2 != r3 != r1:
        print('Escaleno!')
    elif r1 == r2 != r3 or r2 == r3 != r3:
        print('Isósceles!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
