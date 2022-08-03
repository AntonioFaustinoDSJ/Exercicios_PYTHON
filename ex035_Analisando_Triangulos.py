r1 = float(input('1º VALOR: '))
r2 = float(input('2º VALOR: '))
r3 = float(input('3º VALOR: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes valores podem formar um triângulo.')
else:
    print('Não é possível formar um triângulo com estes valores')
