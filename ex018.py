from math import cos, sin, tan, radians
ang = int(input('Digite um ângulo: '))
print(f'{ang} em Seno é: {sin(radians(ang)):.2f}')
print(f'{ang} em Cosseno é: {cos(radians(ang)):.2f}')
print(f'{ang} em Tangente é: {tan(radians(ang)):.2f}')
