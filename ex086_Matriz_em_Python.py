matriz = [[], [], []]

for check1 in range(0, 3):
    for check2 in range(0, 3):
        val = int(input(f'VALOR PARA [{check1},{check2}]:  '))
        matriz[check1].append(val)

print()
for check1 in range(0, 3):
    for check2 in range(0, 3):
        print(f' {matriz[check1][check2]} ', end=' ')
    print()
