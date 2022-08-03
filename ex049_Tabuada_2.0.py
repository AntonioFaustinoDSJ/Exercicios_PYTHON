print()
print('*'*20, 'TABUADA', '*'*21)
tab = int(input('TABUADA DO NÚMERO: '))
ate = int(input('ATÉ O NÚMERO: '))
print()
for c in range(0, ate+1):
    print('{} X {} = {}'.format(tab, c, tab*c))