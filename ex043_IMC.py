print()
peso = float(input('PESO: '))
altu = float(input('ALTURA: '))
print()

imc = peso/(altu**2)

print('IMC {:.2f} - '.format(imc), end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('ACIMA DO PESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else: print('OBESIDADE MORBIDA')