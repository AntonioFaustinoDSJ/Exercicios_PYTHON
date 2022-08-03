verif = str(input('Digite a expressão matemática: '))
contAb = int()
contFech = int()

for check in range(0, len(verif)):
    if verif[check] == '(':
        contAb += 1
    if verif[check] == ')':
        contFech += 1

if contAb != contFech:
    print()
    print('A expressão está errada!')
else:
    print()
    print('A expressão está correta!')
