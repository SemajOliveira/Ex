preço = float(input('Digite o preço do produto: R$ '))
print("""\nComo você vai pargar?
1- À vista com dinheiro/cheque tem 10% de desconto
2- À vista no cartão tem 5% de desconto
3- Em até 2X no cartão o preço é normal
4- 3X ou mais no cartão temos juros de 20%\n""")
escolha = int(input('Digite a opção esolhida: '))

if escolha == 1:
    desconto = preço - (preço * 10/100)
    print(f'Com 10% de desconto o preço do produto fica R$ {desconto}')
elif escolha == 2:
    desconto = preço - (preço * 5/100)
    print(f'Com 5% de desconto o preço do produto fica R$ {desconto}')
elif escolha == 3:
    parcela = preço / 2
    print(f'Em 2X você terá parcelas no valor de R$ {parcela}')
elif escolha == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {totparc}X de R${parcela:.2f} com 20% de juros')
else:
    print('Opção Inválida, Tente novamente...')
print(f'Sua compra de R${preço:.2f} vai custar R${total:.2f} no final')