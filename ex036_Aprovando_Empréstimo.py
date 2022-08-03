print()
print('-=-'*10, 'PROJETO CASA DOS SONHOS', '-=-'*10)

casa = float(input('VALOR DA CASA: R$ '))
sala = float(input('SALÁRIO DO COMPRADOR: R$ '))
anos = float(input('TEMPO PARA PAGAR EM ANOS: '))
entra = float(input('VALOR DE ENTRADA: '))

juros = (casa-entra)+((casa-entra)/100)*15
relacao = juros/(anos*12)

if relacao > ((sala / 100) * 30) or entra < ((casa / 100) * 15):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('{:.0f} parcelas de R$ {:.2f}'.format(anos*12, relacao))
    print('EMPRÉSTIMO CONCEDIDO!')

