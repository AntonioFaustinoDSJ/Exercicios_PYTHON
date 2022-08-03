from time import sleep
print('-=-'*15)
print()
print('VIAGENS DE ATÉ 200 KM: R$ 0,75 por KM')
print('CADA KM A MAIS CUSTARÁ APENAS R$ 0,50 ')
print()
print('-=-'*15)
dst=float(input('Qual a distancia de sua viagem? (KM) '))
print('CALCULANDO', end='')
sleep(1) #1 = quantida de segundos que o programa ira dormir
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print()
print('-=-'*15)
if dst <= 200:
    vf=dst*0.75
    print('SUA VIAGEM DE {} KM CUSTARÁ {:.2f}'.format(dst, vf))
else:
    vf=dst-200
    vff=(vf*0.5)+(200*0.75)
    print('SUA VIAGEM DE {} KM CUSTARÁ {:.2f}'.format(dst, vff))
print('-=-'*15)