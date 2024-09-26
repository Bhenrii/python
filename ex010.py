altura = float(input('Altura da sua parede: '))
largura = float(input('Largura da sua parede: '))

area = largura * altura
tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, area))
print('para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))