frase=str(input('DIGITE O SEU NOME: ')).strip()
print('Seu nome em caixa alta é: {}'.format(frase.upper()))
print('Seu nome em caixa baixa é: {}'.format(frase.lower()))
print('Tudo minúsculo menos a primeira letra: {}'.format(frase.capitalize()))
print('Deixa a primeira letra de cada palavra maiúscula: {}'.format(frase.title()))
f2=frase.split()
print('Seu primeiro nome é {} e tem {} letras'.format(f2[0], len(f2[0])))
print('Seu nome possui um total de {} palavras'.format(len(f2[0:])))
print('Seu nome possui um total de {} letras'.format(len(frase) - frase.count(' ')))
print('Seu nome possui {} letras "A"'.format(frase.upper().count('A'))) #Python é Keysensitive, então para verificar
# a presença de uma letra especifica é legal transformar toda a str em maiusculo antes
print('Seu nome pulando de 2 em 2 fica: {}'.format(frase[::2]))
#frase.strip vai remover todos os espaços excedentes no começo e no final da str
