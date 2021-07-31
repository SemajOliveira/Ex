frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
#inverso = ''
inverso = junto[::-1]

if inverso == junto:
    print('Temos um Palindromo')
else:
    print('A frase digitada não é um palidromo')
