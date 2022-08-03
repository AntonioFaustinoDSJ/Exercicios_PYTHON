gen = str()
cm = cf = ct = cc = int()

while True:
    print()
    print(' ---------------------------- ')
    print(' --- CADASTRE UMA PESSOA --- ')
    print()
    idade = int(input(' --- Idade: '))
    gen = str(input(' --- Gênero [M/F]: ')).upper().strip()

    while gen not in 'FM':
        print('Tecla invalida.')
        gen = str(input(' --- Gênero [M/F]: ')).upper().strip()

    if (idade >= 18) and (gen == 'M'):
        cm += 1
        ct += 1
    elif (idade >= 18) and (gen == 'F'):
        cf += 1
        ct += 1
    elif idade <= 13:
        cc += 1

    print()
    print(' ---------------------------- ')
    print()
    cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    while cont not in 'NS':
        cont = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if cont == 'N':
        break
        print('FIM DO PROGRAMA. OBRIGADO')


print('Há um total de {} pessoas maiores de idade,'.format(ct))
print('sendo {} HOMENS e {} MULHERES.'.format(cm, cf))
print('Também há um total de {} crianças com 13 anos ou menos'.format(cc))
