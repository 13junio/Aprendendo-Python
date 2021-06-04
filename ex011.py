larg = float(input('Qual é a largura da parede? '))
alt = float(input('Qual é a altura da parede? '))
área = larg * alt
print('A parede tem dimensões de {}x{} e a sua área é de {}m'.format(larg, alt, área))
tinta = área / 2
print('Para você pintar a parede, você vai precisar de {}l de tinta'.format(tinta))
