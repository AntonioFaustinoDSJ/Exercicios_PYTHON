print('')
nome = input ('Digite o seu nome! ')
print('')
print('Seja bem-vindo {:>25}!!'.format(nome)) #o nome vai ser escrito em 20 caracteres alinhados para esquerda

print('')
sobre = input ('Digite o seu sobrenome! ')
print('')
print('Então você é o Sr(a) {:*^25}?'.format(sobre)) #o nome vai ser centralizado e preenchido com *

print('')
idade = input('Quantos anos você tem? ')
print('')
print('Você ainda é jovem! \n Tem apenas {} anos e se chama {}!'.format(idade,nome+sobre), end='')
#o \n quebra a linha e o ,end='' interrompe a quebra. O que é colocado depois do = do end vai ser printado na .igação entre as linhas
print (' Até mais, Jovem Gafanhoto!')