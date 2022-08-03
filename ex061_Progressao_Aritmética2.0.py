v = int(input('PRIMEIRO TERMO: '))
r = int(input('RAZÃO DA P.A.: '))
c = int(0)
while c < 10:
    print(v, '-> ', end='')
    v += r
    c += 1
print('FIM')