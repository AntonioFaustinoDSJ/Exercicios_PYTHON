from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
for valor in numeros:
    print(f'{valor}', end=' ')
#neste for o 'valor' indica o contador que vai ser verificado dentro dos slots de 'numeros'
    #exemplo, quando o valor for 1 ele vai imprimir o valor que esta dentro do slot 1 de numeros


print()

print(f'O maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')