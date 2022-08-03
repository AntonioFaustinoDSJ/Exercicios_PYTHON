print()
print('PROGRESSÃO ARITMÉTICA')
print()
pt = int(input('Primeiro Termo: '))
rz = int(input('Razão: '))
qt = int(input('Quantidade de Termos: '))
print()
for c in range(0, qt):
    print(pt, end=' → ')
    pt = pt + rz
    if c == qt-1:
        print('ACABOU!')