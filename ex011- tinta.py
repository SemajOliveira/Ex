alt = float(input('Digite a altura da parede: '))
larg = float(input('Digite a largura da parede: '))
área = alt * larg
print(f'Sua parede mede {larg}X{alt} e sua área é de {área}m²')
tinta = área / 2
print(f'Para pintar essa parede, você precisará de {tinta} l de tinta')
