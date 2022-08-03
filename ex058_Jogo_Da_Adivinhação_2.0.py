import random
print()
print('HUM Aqui é HPniac, seu COMPUTADOR. Vamos brincar de adivinhação?')
print('Eu pensei em um número de 0 a 10. Será que você consegue adivinhá-lo?')
print()
adv = int(input('Qual é o seu 1º palpite?... '))

cp = random.randint(0,10)
cnt = int(1)

while adv != cp:
    if adv < cp:
        cnt += 1
        print()
        print('HUM... Tente um número maior')
        adv = int(input('Tentativa número {} é... '.format(cnt)))
    if adv > cp and adv <= 10:
        cnt += 1
        print()
        print('HUM... Tente um número menor')
        adv = int(input('Tentativa número {} é... '.format(cnt)))
    if adv > 10:
        cnt += 1
        print()
        print('Ser inferior repugnante! Escolha apenas valores de 0 a 10. ')
        adv = int(input('Tentativa número {} é... '.format(cnt)))

print()
if adv == cp and cnt <= 3:
    print('GRR! Congratulações, humano! Você acertou. Ambos pensamos no número {}'.format(cp))
    print('Você teve {} tentativas e sua pontuação foi {}'.format(cnt, 100-cnt*10))
elif adv == cp and cnt > 3:
    print('Rsrs... Você sofreu, mas conseguiu acertar. Ambos pensamos no número {}'.format(cp))
    print('Você teve {} tentativas e sua pontuação foi {}'.format(cnt, 100-cnt*10))
