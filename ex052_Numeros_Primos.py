print()
print('IDENTIFICADOR DE NÚMEROS PRIMOS')
print()
num = int(input('Digite o número: '))
print()
c2 = int(0)
for c in range(1, num + 1):
    if num % c == 0:
        c2 = c2 + 1
        print('\33[1;31m', end=' ')
        print(c, end=' ')
    else:
        print('\33[32m', end=' ')
        print(c, end=' ')
print('\33[m')
if c2 == 2:
    print('O #{} é um NÚMERO PRIMO, já que ele foi divido por 1 e por ele mesmo.'.format(num))
else:
    print('O #{} NÃO é um número primo, já que ele foi divido {} vezes.'.format(num, c2))
