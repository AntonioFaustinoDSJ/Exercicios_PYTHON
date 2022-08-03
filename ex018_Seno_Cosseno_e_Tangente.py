import math
ang=float(input('Digite um ângulo: '))
seno=math.sin(math.radians(ang))
print('O SENO DE {} É {:.2f}'.format(ang, seno))
cosseno=math.cos(math.radians(ang))
print('O COSSENO DE {} É {:.2f}'.format(ang, cosseno))
tangen=math.tan(math.radians(ang))
print('A TANGENTE DE {} É {:.2f}'.format(ang, tangen))
