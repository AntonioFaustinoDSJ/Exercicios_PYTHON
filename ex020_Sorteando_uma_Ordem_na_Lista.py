import random
print('*'*20, 'ORDEM DE APRESENTAÇÃO ', '*'*20)
a1=str(input('Primeiro Aluno: '))
a2=str(input('Segundo Aluno: '))
a3=str(input('Terceiro Aluno: '))
a4=str(input('Quarto Aluno: '))
a5=str(input('Quinto Aluno: '))
print('')
lista=[a1, a2, a3, a4, a5]
format(random.shuffle(lista))
print(lista)