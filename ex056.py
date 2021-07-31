media = cont = 0
for i in range(1, 5):
    nome = str(input(f'Nº {i} Digite seu nome: '))
    idade = int(input((f'Nº {i} Digite sua idade: ')))
    sexo = str(input('Digite seu sexo[Masculino/ Feminino]: ')).strip().lower()[0]
    media += idade / 4
    if sexo == 'f' and idade < 20:
        cont += 1

    if i == 1 and sexo in 'm':
        maiorIdadeHomem = idade
        homemVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        homemVelho = nome
print(f'A média de idade do grupo é: {media}')
print(f'O homem mais velho tem {maiorIdadeHomem} e seu nome é {homemVelho}')
print(f'São {cont} mulheres com menos de 20 anos')
