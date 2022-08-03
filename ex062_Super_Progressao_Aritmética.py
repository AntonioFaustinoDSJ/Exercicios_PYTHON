v = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO DA P.A.: '))
c = int(0)
c2 = int(0)
c3 = int(0)
while c < 10:
    print(v, '-> ', end='')
    v += r
    c += 1
print('PAUSA')
c = int(input('Deseja ver mais quantos resultados? '))
c3 += c
while c2 < c:
    print(v, '-> ', end='')
    v += r
    c2 += 1
    if c2 == c:
        print('PAUSA')
        c = int(input('Deseja ver mais quantos resultados? '))
        c3 += c
        c2 = 0
        if c == 0:
            c3 += 10
            print('Progressão finalizada com {} termos mostrados'.format(c3))