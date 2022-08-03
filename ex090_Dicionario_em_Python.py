alunos = {}

print()
alunos['NOME'] = str(input('Nome do aluno: '))
alunos['MÉDIA'] = int(input('Média anual deste aluno: '))

if alunos['MÉDIA'] >= 7:
    alunos['SITUAÇÃO'] = 'APROVADO!'

elif (alunos['MÉDIA'] >= 5) and (alunos['MÉDIA'] < 7):
    alunos['SITUAÇÃO'] = 'RECUPERAÇÃO!'

else:
    alunos['SITUAÇÃO'] = 'REPROVADO!'

print()
print('-=-' * 10)
print()
for key, value in alunos.items():
    print(f'{key} = {value}')
