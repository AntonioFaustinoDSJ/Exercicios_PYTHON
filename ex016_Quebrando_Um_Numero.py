import math
val=float(input('Digite um valor quebrado: '))
print('A porção inteira de {} é {}'.format(val, math.trunc(val))) #Está função expoe apenas a parte inteira do valor

val2=float(input('Digite outro valor quebrado: '))
print('A porção inteira de {} é {}'.format(val2, int(val2)))

print('Assim também funciona {:.0f}'.format(val2))