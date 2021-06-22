frase = input('Digite uma frase: ').strip().lower()
#letras com acento não serão contabilizadas
print(f'A letra \"A\" aparece \033[32m{frase.count("a")}\033[m vezes')
#o +1 é porque o computador começa a contar do zero
print(f'A letra \"A\" aparece a primeira vez na posição \033[32m{frase.find("a")+1}\033[m')
print(f'A letra \"A|" aparece a última vez na posição \033[32m{frase.rfind("a")+1}\033[m')

