nome = input('Digite seu nome completo: ').strip()
#nome apenas com caracteres maiúsculo
print(f'Nome em maiúsculo: {nome.upper()}')

#apenas com caracteres minúsculo
print(f'Nome em minúsculo: {nome.lower()}')

#total de letras sem considerar espaços, apenas caracteres
print(f'Seu nome ao todo tem: {len(nome) - nome.count(" ")} letras')

corte = nome.split()
print(f'Seu primeiro nome tem {len(corte[0])} letras')
