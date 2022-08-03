print()
print('-=-'*7, 'CONVERSOR DE BASES NUMÉRICAS', '-=-'*7)

num = int(input('VALOR A SER CONVERTIDO: '))
print()
print('Escolha uma das bases para conversão:')
print()
print('[1] BINÁRIO')
print('[2] OCTAL ')
print('[3] HEXADECIMAL')
esc = int(input('ESCOLHA: '))
print()

if esc == 1:
    print('{} em BINÁRIO é: {}'.format(num, bin(num)[2:])) #é necessário usar o [2:] para fatiar a string e remover os
    # dois primeiros digitos q não sao necessarios
elif esc == 2:
    print('{} em OCTAL é: {}'.format(num, oct(num)[2:]))
elif esc == 3:
    print('{} em HEXADECIMAL é: {}'.format(num, hex(num)[2:]))
else:
    print('OPÇÃO INVALIDA')
