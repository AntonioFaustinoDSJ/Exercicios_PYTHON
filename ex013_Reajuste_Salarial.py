sal=float(input('Insira o seu salário \n R$ '))
aju=float(input('Insira o ajuste (%): '))
nsal=sal*(aju/100)
print('O salário de R$ {}, com ajuste de {}% \nserá de R$ {:.2f}'.format(sal,aju,sal+nsal))
print('O total do aumento foi de R$ {}'.format(nsal))