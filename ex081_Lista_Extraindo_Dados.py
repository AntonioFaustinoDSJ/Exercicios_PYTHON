lista = []
check = str()
check3 = int()

while check != 'N':
    val = int(input('Digite um valor: '))
    check = input('Deseja continuar: [S/N]: ').strip().upper()
    lista.append(val)
    print()

print()
print(f'Você digitou {len(lista)} valores')
lista.sort(reverse=True)
print('A lista em ordem decrescente é ', lista)

verif = int(input('Qual valor você gostaria de verificar na lista? '))

for check2 in range(0, len(lista)):
    if lista[check2] == verif:
        print()
        print('Sim, este valor está na lista')
        check3 += 1
        break
if check3 == 0:
    print()
    print('Não, este valor não está na lista')