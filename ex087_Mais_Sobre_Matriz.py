matriz = [[], [], []]
somPar = mr = int(0)

for check1 in range(0, 3):
    for check2 in range(0, 3):
        val = int(input(f'VALOR PARA [{check1},{check2}]:  '))
        matriz[check1].append(val)
        if val % 2 == 0:
            somPar += val

print()
for check1 in range(0, 3):
    for check2 in range(0, 3):
        print(f' {matriz[check1][check2]} ', end=' ')
    print()

print()
print(f'A soma dos valores pares é {somPar}')
print(f'A soma dos valores da terceira coluna {(matriz[0][2])+(matriz[1][2])+(matriz[2][2])}')

mr = matriz[1][0]
for check in range(0, 3):
    if matriz[1][check] > mr:
        mr = matriz[1][check]
print(f'O maior valor na 2ª coluna é {mr}')