r1 = float(input('1º VALOR: '))
r2 = float(input('2º VALOR: '))
r3 = float(input('3º VALOR: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Estes valores podem formar um triângulo.')
    if r1 == r2 and r1 == r3 and r2 == r3:
        print('Este é um triângulo equilátero')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Este é um triângulo isósceles')
    else: print('Este é um triângulo escaleno')
else:
    print('Não é possível formar um triângulo com estes valores')