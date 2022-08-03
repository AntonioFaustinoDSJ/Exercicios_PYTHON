import datetime
nasc = int(input('ANO DE NASCIMENTO: '))
data = datetime.date.today().year

if data-nasc >= 25:
    print('Atleta de nível MASTER')
elif data-nasc > 19 and data-nasc <= 25:
    print('Atleta de nível SÊNIOR')
elif data-nasc > 14 and data-nasc <= 19:
    print('Atleta de nível INFANTIL')
elif data-nasc <= 9:
    print('Atleta de nível MIRIM')

