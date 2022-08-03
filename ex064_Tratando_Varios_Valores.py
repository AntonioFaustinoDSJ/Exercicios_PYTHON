s = int()
k = int()
c = int(input('Digite um valor: '))
while c != 999:
    s += c
    k += 1
    c = int(input('Digite um valor: '))
print('Você digitou {} valores e a soma deles {}.'.format(k, s))