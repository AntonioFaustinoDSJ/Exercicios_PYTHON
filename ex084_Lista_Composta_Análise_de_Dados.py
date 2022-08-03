paciente = []
pacientesTot = []
mr = mn = float()

while True:

    paciente.append(str(input('NOME: ')))
    paciente.append(float(input('PESO: ')))

    pacientesTot.append(paciente[:])
    paciente.clear()

    check = str(input('ADD NOVA LISTA [S/N]: ')).upper().strip()
    if check == 'N':
        break
    print()

mr = mn = pacientesTot[0][1]
for check2 in pacientesTot:
    if check2[1] >= mr:
        mr = check2[1]

    if check2[1] <= mn:
        mn = check2[1]

print()
print(f'Pesando {mr}KG, a(s) pessoa(s) mais gorda(s): ')

for check2 in pacientesTot:
    if check2[1] == mr:
        print(check2[0])

print()
print(f'Pesando {mn}KG, a(s) pessoa(s) mais magra(s): ')

for check2 in pacientesTot:
    if check2[1] == mn:
        print(check2[0])