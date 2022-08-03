fr = str(input('Escreva uma Frase: ')).strip()
l = str(input('Escolha uma Letra: ')).strip()

fru = fr.upper()
lu = l.upper()

print('Seu nome possui {} letras "{}"'.format(fru.count(lu), lu))
print('A letra "{}" aparece pela primeira vez na posição {}'.format(lu, fru.find(lu)+1)) #o +1 é apenas para ficar
#menos abstrato pois posição '0' é estrnaho
print('A letra "{}" aparece pela última vez na posição {}'.format(lu, fru.rfind(lu)+1))