cid = input('Digite o nome de uma cidade: ').strip().lower()
print(f'A ciade começa com \"SANTO\"? \033[31m{cid[0:5] == "santo"}\033[m')
