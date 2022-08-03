print()
while True:
    print('* '*12, ' T A B U A D A ', '* '*12)
    tab = int(input('Tabuada do número (0 break): '))
    if tab == 0:
        print('FIM DA TABUADA. OBRIGADO')
        break
    ate = int(input('Até o número: '))
    check = int(0)

    while check <= ate:
        print('{} X {} = {}'.format(tab, check, tab*check))
        check += 1


