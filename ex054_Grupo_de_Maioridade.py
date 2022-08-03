import datetime
print()
maior = int(0)
menor = int(0)
atual = datetime.date.today().year
for c in range(1, 8):
    ano = int(input('{}ª ano: '.format(c)))
    verif = atual - ano
    if verif >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print('Há {} pessoa(s) maior(es) de idade e {} pessoa(s) menor(es) de idade'.format(maior, menor))