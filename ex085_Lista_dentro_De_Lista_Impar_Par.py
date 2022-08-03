lista = [[], []]
check = int(1)

while check != 8:
    val = int(input(f'{check}º valor: '))
    check += 1

    if val % 2 == 0:
        lista[0].append(val)
    if val % 2 != 0:
        lista[1].append(val)

lista[0].sort()
lista[1].sort()

print()
print(f'Os números pares são {lista[0]}')
print(f'Os números ímpares são {lista[1]}')