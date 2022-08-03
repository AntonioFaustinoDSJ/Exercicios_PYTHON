#Importante fazer este exercício sem usar sort
lista = []
for check in range(0, 5):
    val = int(input('Digite um número: '))

    if check == 0 or val > lista[-1]:
        lista.append(val)
        print('Valor adicionado ao final da lista...')
        print()

    else:
        check2 = 0
        while check2 < len(lista):
            if val <= lista[check2]:
                lista.insert(check2, val) #vai inserir na posição check2 o valor val
                print(f'Valor adicionado na posição {check2} da lista')
                print()
                break
            check += 1


print('Os valores digitas em ordem são ', lista)
