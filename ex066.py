num = cont = soma = 0
num = int(input('Digite um valor: [999 para parar] '))
while True:
    soma += num
    cont += 1
    num = int(input('Digite um valor: [999 para parar] '))
    if num == 999:
        break
print(f'Você digitou {cont} números e  a soma entre eles foi {soma}')
