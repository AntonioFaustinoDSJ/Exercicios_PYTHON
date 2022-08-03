print('')
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

soma = n1+n2
div = n1/n2
divi = n1//n2

print('')
print('A soma de {} + {} = {}'.format(n1,n2,soma))

print('')
print ('A multiplicação de', n1, 'X', n2, '= {}'.format(n1*n2))

print('')
print ('A divisão entre {} e {} é igual a {:.3f} e a divisão inteira é {}'.format(n1,n2,div, divi))
#o :.3f indica que o valor vai aparecer em 3 casas depois da virgula com valor flutuante
