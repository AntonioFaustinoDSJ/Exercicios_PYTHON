check = str()
listaT = []
listaP = []
listaI = []

while check != 'N':
    val = int(input('VALOR: '))
    listaT.append(val)

    if val % 2 == 0:
        listaP.append(val)

    if val % 2 != 0:
        listaI.append(val)

    check = str(input('Deseja add outro valor? [S/N]: ')).upper().strip()
    print()

print(f'A lista de valores pares é: {listaP}')
print(f'A lista de valores ímpares é: {listaI}')
print(f'A lista total é: {listaT}')