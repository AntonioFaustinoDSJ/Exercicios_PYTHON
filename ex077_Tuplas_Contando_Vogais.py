comandantes = ('Nekusar', 'Zacama', 'Estrid', 'Aminatou', 'Melstrom', 'Otrimi', 'WindGrace')
for p in comandantes:
    print('\n No comandante', p, ' temos: ')
    for letra in p:
        if letra in 'aeiouAEIOU':
            print(letra, end=' ')