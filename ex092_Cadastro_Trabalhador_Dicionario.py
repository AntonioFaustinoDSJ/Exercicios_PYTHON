ctps = {}

print()
ctps['NOME'] = str(input('Nome do trabalhador: '))
ctps['ANO'] = int(input('Ano de nascimento: '))
ctps['CTPS'] = int(input('Número da carteira (0 se não tiver): '))

if ctps['CTPS'] != 0:
    ctps['CONTRATAÇÃO'] = int(input('Ano da contratação: '))
    ctps['SALÁRIO'] = int(input('Salário: '))
    ctps['APOSENTADORIA'] = (ctps['CONTRATAÇÃO'] + 35)-ctps['ANO']

print()
for key, value in ctps.items():
    print(f'{key} = {value}')

