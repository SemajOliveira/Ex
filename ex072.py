valores = ('Zero', 'Um', 'Dois', 'Três', 'Quatro',
'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
'Dez', 'Onze', 'Doze', 'Treze', 'Quatoze',
'Quinze', 'Desseseis', 'Dezesete', 'Dezoito',
'Dezenove', 'Vinte')
print(valores)

while True:
    try:
        n = int(input('Digite um valor inteiro[ Entre 0 e 20]: '))
        if n == int(n):
            print(f'Seu número extenso é: {valores[n]}')
    except:
        print('Entrada inválida')

    op = input('Você quer continuar?[Sim/ Não] ').strip().lower()[0]
    if op == 'n':
        print('Programa encerrado...')
        break 
