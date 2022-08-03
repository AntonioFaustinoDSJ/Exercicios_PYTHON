itensEpreços = ('Lápis', '1.00', 'Borracha', '1.75', 'Caneta', '2.00', 'Estojo',
                '25.75', 'Caderno', '18.00', 'Mochila', '128.50', 'Lancheira', '28.00')
check = int()

print()
print('-' * 45)
print(' ' * 15, '* PAPELARIA *', ' ' * 15)
print('-' * 45)
print()

while True:
    print(itensEpreços[check*2],
          '.' * (32 - len(itensEpreços[check*2])),
          'R$',' '*(6 - len(itensEpreços[check*2+1])),itensEpreços[check*2+1])
    check += 1
    if check == len(itensEpreços) // 2:
        break

print()
print('-' * 45)