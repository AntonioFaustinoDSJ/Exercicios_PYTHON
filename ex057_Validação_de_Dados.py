print()

gen = str('x')
while (gen != 'M') and (gen != 'F'):
    gen = str(input('Informe o seu gênero (M/F): ')).upper().strip()
    print()
print('Gênero ', gen, ' registrado com sucesso!')