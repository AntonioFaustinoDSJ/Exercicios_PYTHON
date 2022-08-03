v1 = int(input('1º VALOR: '))
v2 = int(input('2º VALOR: '))
v3 = int(input('3º VALOR: '))
if v1 > v2 and v1 > v3:
    print('{} É o maior valor'.format(v1))
    if v2 > v3:
        print('{} É o menor valor'.format(v3))
    else:
        print('{} É o menor valor'.format(v2))

if v2 > v1 and v2 > v3:
    print('{} É o maior valor'.format(v2))
    if v1 > v3:
        print('{} É o menor valor'.format(v3))
    else:
        print('{} É o menor valor'.format(v1))

if v3 > v1 and v3 > v2:
    print('{} É o maior valor'.format(v3))
    if v3 > v1:
        print('{} É o menor valor'.format(v1))
    else:
        print('{} É o menor valor'.format(v2))
