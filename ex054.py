from datetime import date
atual = date.today().year
totmaior = totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}ª você nasceu? '))
    idade = atual - nasc
    if idade >= 21:
       totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} maiores de idade e {totmenor} menores de idade!')

