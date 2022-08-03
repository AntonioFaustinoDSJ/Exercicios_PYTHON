check = str()
c = s = mn = mr = int(0)

while check != 'N':
    n = int(input('Digite um valor: '))
    check = str(input('Deseja continuar [S/N]: ')).upper().strip()
    c += 1
    s += n
    if c == 1:
        mn = mr = n
    if n > mr:
        mr = n
    if n < mn:
        mn = n

print('Você digitou {} números cuja soma é {} e a média é {}'.format(c, s, s/c))
print('O maior número digitado foi o {} e o menor foi {}'.format(mr, mn))
