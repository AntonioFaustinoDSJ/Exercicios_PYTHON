from random import randrange
print('')
print('-=-'*10, 'RADAR ELETRONICO', '-=-'*10)
radar=randrange(10,160,5) #randrage gera numeros aleatorios com intervalo (n1,n2,intervalo)
print('')
print('O RADAR DETECTOU QUE SUA VELOCIDADE ATUAL É DE: {} KM/H'.format(radar))
if radar > 80:
    print('RISCO! Você está acima da velocidade máxima de 80 KM/H')
    multa=(radar-80)*7
    print('Você será multado em R$ {}!'.format(multa))
else:
    print('Você está abaixo da velocidade máxima, contimue assim.')
print('')
print('-=-'*26)