print('*'*15, 'VALOR DO ALUGUEL', '*'*15)
dia=float(input('DIAS DE ALUGUEL: '))
km=float(input('QUILÔMETROS RODADOS: '))
valf=(dia*60)+(km*0.15)
print('TOTAL A PAGAR -> R$ {:.2f}'.format(valf))