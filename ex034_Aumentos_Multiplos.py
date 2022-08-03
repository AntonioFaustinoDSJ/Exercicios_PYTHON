sal = float(input('SALÁRIO INICIAL: R$ '))
if sal <= 1212:
    porc = 18
    aumen = (sal/100)*porc
    salf = aumen + sal
else:
    porc = 12
    aumen = (sal/100)*porc
    salf = aumen + sal
print('O aumento foi de {}%. O salário de R$ {} se tornou R$ {:.2f}'.format(porc, sal, salf))