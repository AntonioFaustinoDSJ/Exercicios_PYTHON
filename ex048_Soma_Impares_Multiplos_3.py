print()
print()
soma = int(0)
contagem = int(0)
print('SOMA ENTRE TODOS OS NÚMEROS ÍMPARES MULTIPLOS DE 3 NO INTERVALO DE 1 A 500 É:')
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        contagem = contagem +1
print('Temos {} valores que somados somados são {}1'.format(contagem, soma))