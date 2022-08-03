print()
print(' ----- CALCULADORA DE FATORIAL ---- ')
print()
fat = int(input('ESCOLHA UM VALOR: '))
fatc = fat
for c in range (fatc-1, 1, -1):
    fat = fat * c
print('O Fatorial de {} é {}'.format(fatc, fat))