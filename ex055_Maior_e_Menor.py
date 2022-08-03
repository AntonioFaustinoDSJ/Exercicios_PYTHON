verif1 = float(0)
verif2 = float(1000)
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa (KG): '.format(c)))
    if peso > verif1:
        verif1 = peso
    if peso < verif2:
        verif2 = peso
print("O maior peso é {}KG e o menor é {}KG".format(verif1, verif2))
