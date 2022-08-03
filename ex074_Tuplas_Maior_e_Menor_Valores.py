import random
val = (0,1,2,3,4,5,6,7,8,9,10)
print()
for check in range(0,5):
    vAle = random.choice(val)
    print(vAle, end=' ')
    if check == 0:
        mr = mn = vAle
    if vAle > mr:
        mr = vAle
    if vAle < mn:
        mn = vAle
    if check == 4:
        print()

print()
print('O maior valor sorteado foi ', mr)
print('O menor valor sorteado foi ', mn)