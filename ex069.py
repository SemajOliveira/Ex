cont = mulher = homem = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = input('Digite seu sexo: [Masculino/Feminio] ').strip()
    op = str(input('você quer continuar? [Sim/Não] ')).strip().lower()[0]
    if idade > 18:
        cont += 1
    if sexo == 'm':
        homem += 1
    if sexo == 'f' and idade < 20:
        mulher += 1 

    if op == 'n':
        break

print(f'{cont} pessoas tem mais de 18 anos ')
if homem == 1:
    print('Foi cadastrado 1 homem apenas')
else:
    print(f'Foram cadastrados {homem} homens')

if mulher == 1:
    print('Foi cadastrado uma mulher apenas')
else:
    print(f'Foram cadastradas {mulher} mulheres com menos de 20 anos')


