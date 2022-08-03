print()
print('SOMAREI APENAS OS 7 VALORES PARES QUE VOCÊ DIGITAR!')
print()
val2 = int(0)
for c in range(1, 8):
    val = int(input('{}º VALOR: '.format(c)))
    if val % 2 == 0:
        val2 = val + val2
print()
print('A SOMA DE TODOS OS VALORES PARES É: {}'.format(val2))