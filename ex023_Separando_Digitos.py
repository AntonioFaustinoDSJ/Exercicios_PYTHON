n=int(input('INFORME UM NÚMERO: '))
u=n//1%10
d=n//10%10
c=n//100%10
m=n//1000%10
print('Analisando {}...'.format(n))
print('UNIDADES: {}'.format(u))
print('DEZENAS: {}'.format(d))
print('CENTENAS: {}'.format(c))
print('MILHARES: {}'.format(m))