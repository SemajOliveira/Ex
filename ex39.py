from datetime import date
ano = int(input('Digite o ano que você nasceu: '))
atual = date.today().year
idade = atual - ano
genero = input('Digite seu sexo[Masculino/Feminino]: ').strip().lower()[0]
if genero == 'm':
    if idade < 18:
        saldo = 18 - idade
        print(f'Faltam {saldo} para você se alistar')
    elif idade == 18:
        print(f'É a hora de se alistar')
    elif idade > 18:
        saldo = idade - 18 
        print(f'Você já passou {saldo} anos do tempo de alistamento')
else:
    print('Mulheres não são obriagadas a prestarem serviço militar!')
