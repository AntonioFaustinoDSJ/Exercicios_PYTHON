from math import hypot
print('-'*21)
cato=float(input('CATETO OPOSTO: '))
print('')
cata=float(input('CATETO ADJACENTE: '))
print('-'*21)
print('O VALOR DA HIPOTENUSA É {:.2f}'.format(hypot(cato,cata)))