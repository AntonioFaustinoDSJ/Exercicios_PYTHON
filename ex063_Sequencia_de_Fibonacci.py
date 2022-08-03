f = int(input('Quantos termos você quer mostrar? '))
t = int(0)
a = 0
b = 1
c = 0
print(a, b, end=' ')
while t < f-2:
    t += 1
    c = a + b
    a = b
    b = c
    print(c, end=' ')
