soma = cont = val = int(0)
while True:
    soma += val
    val = int(input('Digite um valor para somar (999 break): '))
    if val < 999:
        cont += 1
    if val == 999:
        break
print('A soma dos {} valores digitados é {}'.format(cont, soma))