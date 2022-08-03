print()
palavra = str(input('Digite uma palavra: ')).strip().upper()
separar = palavra.split()
juntar = ''.join(separar)  # os '' servem para indicar o que voce quer colocar separando as palavras, neste caso, por esrar vazio, elas simplemnetes irao se separar
inverso = ''
print()
for c in range(len(juntar) - 1, -1, -1):
    inverso += juntar[c]
print('{} ao contrário é {}'.format(juntar, inverso))
if juntar == inverso:
    print('{} é um palíndromo'.format(juntar))
else:
    print('{} não é um palíndromo'.format(juntar))

