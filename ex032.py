from datetime import date
#ano atual da máquina


ano = int(input('Digite o ano para a análise [0 para o ano atual]: '))

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Ano {ano} é BISSEXTO')

else:
    print(f'Ano {ano} não é BISSEXTO')