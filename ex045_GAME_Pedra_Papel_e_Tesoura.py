import random
print()
print('|', '-=-'*7, 'JOKENPÔ', '-=-'*7, '|')
print('|                  ~*~  ESCOLHA  ~*~                  |')
print('|  ~~ [ 1 ] Pedra                                     |')
print('|  ~~ [ 2 ] Papel                                     |')
print('|  ~~ [ 3 ] Tesoura                                   |')
print('|                                                     |')
escolha = int(input('SELECIONE: '))

if escolha == 1:
    jkp = str('Pedra')
elif escolha == 2:
    jkp = str('Papel')
elif escolha == 3:
    jkp = str('Tesoura')

complista = [1, 2, 3]
compale = random.choice(complista)

if compale == 1:
    jkpc = str('Pedra')
elif compale == 2:
    jkpc = str('Papel')
elif compale == 3:
    jkp = str('Tesoura')

print()
print('Você escolheu {} \nO Computador escolheu {}'.format(jkp, jkpc))
print()

a = str('VOCÊ VENCEU!!!')
b = str('O COMPUTADOR VENCEU!!!')

if jkp == jkpc:
    print('EMPATE!!!')
elif jkp == 'Pedra' and jkpc == 'Papel':
    print(b)
elif jkp == 'Pedra' and jkpc == 'Tesoura':
    print(a)
elif jkp == 'Papel' and jkpc == 'Pedra':
    print(a)
elif jkp == 'Papel' and jkpc == 'Tesoura':
    print(b)
elif jkp == 'Tesoura' and jkpc == 'Papel':
    print(a)
elif jkp == 'Tesoura' and jkpc == 'Pedra':
    print(b)


