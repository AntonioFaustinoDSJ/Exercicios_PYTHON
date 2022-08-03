lista = []
check = str()
cnt = int(0)
while check != 'N':
    num = int(input('Adicione o valor: '))

    if num not in lista: #verifica se o valor esta na lista, se nao estiver = true
        lista.append(num)
    else:
        print('Valores repetidos não serão salvos!')

    check = str(input('Continuar? [S/N]: ')).strip().upper()
    print()

print(sorted(lista))