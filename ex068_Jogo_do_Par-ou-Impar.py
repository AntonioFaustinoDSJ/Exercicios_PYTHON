import random
pts = int()
print()
print('-=-'*5, 'JOGO DO PAR OU IMPAR', '-=-'*5)

while True:

    val = int(input('Diga um valor [0-10]: '))
    pi = str('X')
    pi = str(input('Par ou ímpar? [P/I]: ')).upper().strip()

    while pi not in 'PI':
        print('Você digitou um valor invalido. Tente novamente.')
        pi = str(input('Par ou ímpar? [P/I]: ')).upper().strip()

    pcval = random.randint(0,10)
    soma = pcval + val
    div = soma % 2

    if div == 0:
        resul = 'P'
        resul2 = 'PAR'
    else:
        resul = 'I'
        resul2 = 'ÍMPAR'

    if resul == pi:
        pts += 1
        print('Você escolheu {} e o PC {}. A soma deles é {}, um número {}'.format(val, pcval, soma, resul2))
        print('VOCÊ ACERTOU! Parabéns, você ganhou 1 ponto')
        print()

    if pi != resul:
        print('Você escolheu {} e o PC {}. A soma deles é {}, um número {}'.format(val, pcval, soma, resul2))
        print('Que pena, você errou! Seu número de acertos foi ', pts)
        print()
        print('FIM DE JOGO')
        break
