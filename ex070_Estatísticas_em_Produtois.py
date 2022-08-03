print()
caro = barato = tot = c = float()

while True:
    prod = str(input('Nome do produto: '))
    val = float(input('Preço: R$ '))
    tot += val
    c += 1

    if c == 1:
        barato = caro = val
    if val > caro:
        caro = val
    if val < barato:
        barato = val

    check = str(input('Deseja continuar? [S/N]: ')).strip().upper()

    while check not in 'SN':
        print('Letra invalida, tente novamente')
        check = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    print()
    if check == 'N':
        break

print('Obrigado pelas compras. Volte Sempre!')
print()
print('O valor total de suas compras é R$ ', tot)
print('O produto mais caro comprado foi ', caro)
print('O produto mais barato comprado foi ', barato)