from time import sleep
n50 = n20 = n10 = n1 = int()
print()
print('*'*34)
print('***      CAIXA ELETRONICO      *** ')
print('*'*34)
print()
print('   --- Cédulas disponiveis: ')
print('   --- R$50, R$20, R$10 e R$1')
print()
print('*'*34)
saque = int(input('   --- Valor a ser sacado: '))
print()
print('   --- CALCULANDO', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.', end=' ')
sleep(1)
print('.')

n50 = saque // 50
saque -= (n50 * 50)

n20 = saque // 20
saque -= (n20 * 20)

n10 = saque // 10
saque -= (n10 * 10)

n1 = saque

print()
print('   --- Serão sacadas: ')

if n50 != 0:
    print('   --- {} cédula(s) de R$50 '.format(n50))
if n20 != 0:
    print('   --- {} cédula(s) de R$20 '.format(n20))
if n10 != 0:
    print('   --- {} cédula(s) de R$10 '.format(n10))
if n1 != 0:
    print('   --- {} cédula(s) de R$1 '.format(n1))
print()
print('*'*34)
