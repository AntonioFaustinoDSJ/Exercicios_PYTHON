lista = []
sublistas = []
cont = contA = contB = int()
while True:
    nome = str(input('ALUNO: '))
    sublistas.append(nome)
    n1 = float(input('1º BIMESTRE: '))
    sublistas.append(n1)
    n2 = float(input('2º BIMESTRE: '))
    sublistas.append(n2)
    n3 = float(input('3º BIMESTRE: '))
    sublistas.append(n3)
    n4 = float(input('4º BIMESTRE: '))
    sublistas.append(n4)

    media = (n1+n2+n3+n4)/4
    sublistas.append(media)

    lista.append(sublistas[:])
    sublistas.clear()
    cont += 1

    check = str(input('Deseja adicionar outro aluno? [S/N]: ')).upper().strip()
    if check == 'N':
        break

print()
print('[Nº]    [NOME]        [MÉDIA]')
for contA in range(0, cont):
    print(f'[{contA+1}]     {lista[contA][0]}        {lista[contA][5]}')

print()
verif = str(input('Deseja ver as notas detalhadas de algum aluno? [S/N]:  ')).upper().strip()
if verif == 'S':
    while True:
        notas = int(input('Digite o número do aluno: '))
        print(f'As notas de {lista[notas-1][0]} foram:')
        print(f'1º BIMESTRE: {lista[notas-1][1]}')
        print(f'2º BIMESTRE: {lista[notas-1][2]}')
        print(f'3º BIMESTRE: {lista[notas-1][3]}')
        print(f'4º BIMESTRE: {lista[notas-1][4]}')
        print()

        verif2 = str(input('Deseja ver outra nota? [S/N]: ')).upper().strip()
        if verif2 == 'N':
            print()
            print('Obrigado!')
            break
else:
    print()
    print('Obrigado!')