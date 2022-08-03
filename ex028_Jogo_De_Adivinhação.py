import random
from time import sleep
print('')
print('*'*20, 'ADIVINHADOR', '*'*20)
r=random.randint(0,5)
print('')
n=int(input('Em qual número eu estou pensando de 0 a 5?... '))
print('PENSANDO...')
sleep(2) #vai fazer o programa parar por 2 segundos
if n == r:
    print('PARABÉNS! Você adivinhou')
else:
    print('Você errou... eu tinha pensando em {}'.format(r))
print('')
print('*'*53)