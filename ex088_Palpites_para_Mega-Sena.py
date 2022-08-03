from random import randint
sublista = []
lista = []

check = check2 = int(0)
qtd = int(input('Quantos jogos você vai fazer? JOGOS: '))
print()
for check in range(0, qtd):
    for check2 in range(0, 6):
        val = randint(1, 60)
        sublista.append(val)
    sublista.sort()
    lista.append(sublista[:])
    sublista.clear()


for check in range(0, qtd):
        print(f'Jogo {check + 1}: {lista[check]}')