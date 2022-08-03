print()
print('='*21, "FAUSTINO'S GAMES HOUSE", '='*21)
comp = float(input('VALOR DAS COMPRAS: R$'))
print()

print(' === FORMAS DE PAGAMENTO ===')
print(' === [ 1 ] À VISTA DINHEIRO/DÉBITO')
print(' === [ 2 ] À VISTA CRÉDITO')
print(' === [ 3 ] ATÉ 3 X SEM JUROS')
print(' === [ 4 ] MAIS QUE 3 X')
print()
op = int(input(' === Opção: '))
print()

if op == 1:
    if comp < 1500:
        print(' === NOTA FISCAL ===')
        vfinal = comp-(comp/100)*3
        print(' === + R$', comp, ' (subtotal)')
        print(' === - {} (desconto 3%)'.format((comp/100)*3))
        print(' === + {} (total)'.format(vfinal))
    else:
         print(' === NOTA FISCAL ===')
         vfinal = comp-(comp/100)*5
         print(' === + R$', comp, ' (subtotal)')
         print(' === - {} (desconto 5%)'.format((comp / 100) * 5))
         print(' === + R${} (total)'.format(vfinal))

elif op == 2:
    print(' === NOTA FISCAL ===')
    print(' === + R$', comp, ' (subtotal)')
    print(' === (desconto 0%)')
    print(' === + R${} (total)'.format(comp))
elif op == 3:
    qtdx = int(input('Quantas vezes? '))
    print()
    print(' === NOTA FISCAL ===')
    print(' === {} X de {} sem juros. \n === Total de R${}'.format(qtdx, comp/qtdx, comp))
elif op == 4:
    qtdx = int(input('Quantas vezes? '))
    tot = (comp/qtdx)
    tot2 = (tot/100)*3.5
    tot3 = tot+tot2
    print()
    print(' === NOTA FISCAL ===')
    print(' === {} X de {:.2f} com juros de 3.5% ao mês. \n === Total de R${}'.format(qtdx, tot3, tot3*qtdx))
