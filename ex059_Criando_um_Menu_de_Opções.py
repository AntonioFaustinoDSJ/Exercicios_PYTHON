from time import sleep
print()
c = int(0)
print('*' * 25, ' - SMART CALC - ', '*' * 25)
val1 = int(input(' --- 1º VALOR: '))
val2 = int(input(' --- 2º VALOR: '))
print()
while c != 5:
    print(' --- [1] Somar valores')
    print(' --- [2] Multiplicar valores')
    print(' --- [3] Verificação Ímpar/Par')
    print(' --- [4] Adicionar novos valores')
    print(' --- [5] Finalizar')
    print()
    c = int(input('ESCOLHA UMA OPÇÃO: '))
    print()
    if c == 1:
        valf = val1 + val2
        print('{} + {} = {}'.format(val1, val2, valf))
    if c == 2:
        valf = val1 * val2
        print('{} X {} = {}'.format(val1, val2, valf))
    if c == 3:
        if val1 % 2 == 0:
            print(val1, 'é PAR')
        else:
            print(val1, 'é ÍMPAR')
        if val2 % 2 == 0:
            print(val2, 'é PAR')
        else:
            print(val2, 'é ÍMPAR')
    if c == 4:
        val1 = int(input(' --- 1º VALOR: '))
        val2 = int(input(' --- 2º VALOR: '))
    if c == 5:
        print(' --- FINALIZANDO ', end='')
        print('. ', end='')
        sleep(1)
        print('. ', end='')
        sleep(1)
        print('.')
        sleep(1)
    if c != 5:
        print()
        print('*' * 25, ' - SMART CALC - ', '*' * 25)
    else:
        print()
        print('*' * 67)




