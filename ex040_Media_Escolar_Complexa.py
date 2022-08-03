print()
print('*'*59)
print('*'*22, 'MEDIA ESCOLAR', '*'*22)
print('*'*59)
print()
n1 = float(input('NOTA DO 1º BIMESTRE: '))
n2 = float(input('NOTA DO 2º BIMESTRE: '))
n3 = float(input('NOTA DO 3º BIMESTRE: '))
n4 = float(input('NOTA DO 4º BIMESTRE: '))
print()
print('*'*59)
media = (n1+n2+n3+n4)/4

print('MEDIA FINAL = {}'.format(media))
if media >= 7.5 and media <= 9.9:
    print('PARABENS! ALUNO APROVADO!')
elif media == 10:
    print('PARABENS! SUA NOTA FOI PERFEITA')
elif media > 6 and media <= 7.4:
    print('ALUNO APTO À RECUPERAÇÃO')
else:
    print('ALUNO REPROVADO')
print('*'*59)