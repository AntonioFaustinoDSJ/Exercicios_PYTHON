numex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
         'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
num = int(input('DIGITE UM NÚMERO ENTRE 0 E 20: '))
print()
while num > 20:
        print('VALOR INCORRETO, TENTE NOVAMENTE ---')
        num = int(input('DIGITE UM NÚMERO ENTRE 0 E 20: '))
        print()

for check in range(0, len(numex)):
    if check == num:
        print(numex[check])

