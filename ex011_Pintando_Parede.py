alt = float(input('Altura da parede (M): '))
lar = float(input('Largura da parede (M): '))
m2=alt*lar
print('Esta parede possui uma área de {:.2f}M²'.format(m2))
print('Serão necessários {:.2f}L de tinta, \njá que cada litro pinta 2m²'.format(m2/2))
