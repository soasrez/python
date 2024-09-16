altura=int(input('Altura da parede: '))
largura=int(input('Largura da parede: '))

area = altura * largura

tinta = int(area / 2)


print('A quantidade de tinta necessária para pintar uma parede de {}m2 será de {} litros.'.format(area, tinta))