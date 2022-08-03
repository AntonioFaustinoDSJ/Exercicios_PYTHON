print('*'*12, 'LIQUIDA TUDO', '*'*12)
val=float(input('Valor original R$ '))
d5=val*0.05
d10=val*0.10
d25=val*0.25
print('')
print('COM DESCONTO DE R$ {:.2f} (5%) O PRODUTO SAIRÁ POR R$ {:.2f}'.format(d5,val-d5))
print('COM DESCONTO DE R$ {:.2f} (10%) O PRODUTO SAIRÁ POR R$ {:.2f}'.format(d10,val-d10))
print('COM DESCONTO DE R$ {:.2f} (25%) O PRODUTO SAIRÁ POR R$ {:.2f}'.format(d25,val-d25))