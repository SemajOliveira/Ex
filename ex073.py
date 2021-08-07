# Dia 7 de agosto de 2021 - Séria A
br = ['Palmeiras', 'Atlético-MG', 'Bragatino', 'Fortaleza', 
'Flamengo', 'Athletico-PR', 'Ceará SC','Santos', 
'Atlético-Go', 'Bahia', 'Corinthias', 'Fluminense', 
'Juventude', 'Sport Recife', 'Internacional', 
'Cuiabá', 'São Paulo', 'América-MG','Grêmio', 'Chapecoense']


print(f'\033[32mOs cinco primeiro colocados são\033[m: {br[0:5]}')
print(f'\033[32mOs útlimos da tabela são\033[m: {br[-4::1]}')
print(f'\033[32mO chapecoense está na posição\033[m: {br.index("Chapecoense")+1}')
br.sort()
print(f'\033[32mOrdem alfábetica\033[m: {br}')

