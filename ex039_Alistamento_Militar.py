import datetime
nasc = int(input('Ano de Nascimento: '))
data = datetime.date.today().year

if nasc+18 < data:
    print('Seu alistamento foi em {}, corra você está atrasado {} ano(s)!'.format(nasc+18, data-(nasc+18)))
elif nasc+18 == data:
    print('Corra que seu alistamento é neste ano de {}!'.format(data))
else:
    print('Nascidos em {} tem {} anos em {}'.format(nasc, data-nasc, data))
    print('Ainda faltam {} ano(s) para o seu alistamento em {}'.format((nasc+18)-data, nasc+18))
