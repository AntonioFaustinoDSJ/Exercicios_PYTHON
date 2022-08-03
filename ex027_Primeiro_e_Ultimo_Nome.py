nome=str(input('DIGITE SEU NOME COMPLETO: ')).strip().split()
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1])) #Aqui invés de ter sido colocado o numero do ultimo
#espaço do nome, foi criada uma formula para sempre mostrar o valor da ultima posição
#O len(nome) conta a partir de 1, por isso é colocado o menos 1 na frente