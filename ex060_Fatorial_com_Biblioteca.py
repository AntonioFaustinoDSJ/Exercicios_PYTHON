from math import factorial
print()
print(' ----- CALCULADORA DE FATORIAL ---- ')
print()
n = int(input('ESCOLHA UM VALOR: '))
f = factorial(n)
print('O Fatorial de {} é {}'.format(n,f))