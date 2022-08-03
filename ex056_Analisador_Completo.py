print()
print('*'*10, 'ANALISANDO OS CADASTROS', '*'*10)
tidade = float(0)
velho = float(0)
velha = float(0)
cIdadeM = int(0)
cIdadeF = int(0)
for c in range(1,8):
    print()
    nome = str(input(' --- NOME: ')).strip()
    idade = float(input(' --- IDADE: '))
    gen = str(input(' --- GÊNERO (M/F): ')).strip().upper()
    print()
    print('*' * 45)

    tidade = tidade + idade
    if idade < 18 and gen == 'M':
        cIdadeM = cIdadeM + 1
    if idade < 18 and gen == 'F':
        cIdadeF = cIdadeF + 1
    if idade > velho and gen == 'M':
        velho = idade
        nvelho = nome
    if idade > velha and gen == 'F':
        velha = idade
        nvelha = nome

midade = tidade/7

print()
print(' ---- A idade média é: {:.2f} anos'.format(midade))
print(' ---- O Homem mais velho tem {} e se chama {}'.format(velho, nvelho))
print(' ---- A Mulher mais velha tem {} e se chama {}'.format(velha, nvelha))
print(' ---- Ao todo temos {} Mulheres menores de idade'. format(cIdadeF))
print(' ---- E {} Homens menores de idade'.format(cIdadeM))

