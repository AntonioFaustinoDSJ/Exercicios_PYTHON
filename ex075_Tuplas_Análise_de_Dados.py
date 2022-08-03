val1 = int(input('Digite um valor: '))
val2 = int(input('Digite outro valor: '))
val3 = int(input('Digite mais um valor: '))
val4 = int(input('Digite, por fim, mais um valor: '))
valf = (val1, val2, val3, val4)

print()
print('Verifique quantas vezes o valor X apareceu')
x = int(input('Quem é X? '))
print('{} apareceu {} vezes'.format(x, valf.count(x)))

print()
print('Verifique em qual slot Y apareceu')
y = int(input('Quem é Y? '))
print('{} está no slot de número {}'.format(y, valf.index(y)))

print()
print('Os valores pares digitados foram: ')
for check in range(0, 4):
    if valf[check] % 2 == 0:
        print(valf[check], end=' ')