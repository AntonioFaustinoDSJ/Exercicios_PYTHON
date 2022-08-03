lista = []
for check in range(0,5):
    lista.append(int(input(f'Adicione um valor no espaço {check}: ')))
    val = lista[check]
    if check == 0:
        mr = mn = val
    if val > mr:
        mr = val
    if val < mn:
        mn = val

print(f'Os valores presentes na lista são: {lista}')

print(f'O maior valor encontrado é o {mr}, na posição: ', end='')

for check in range(0,5):
    if lista[check] == mr:
        print(check, ' ... ', end='')
print('\n')
print(f'O menor valor encontrado é o {mn}, na posição: ', end='')
for check in range(0,5):
    if lista[check] == mn:
        print(check, ' ...', end='')