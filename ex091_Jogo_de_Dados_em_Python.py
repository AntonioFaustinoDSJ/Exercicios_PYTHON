from random import randint
from time import sleep
from operator import itemgetter

print()
players = {"player1": randint(1, 6),
           "player2": randint(1, 6),
           "player3": randint(1, 6),
           "player4": randint(1, 6)}
ranking = [] #é uma lista

for key, value in players.items():
    print(f'O {key} tirou {value} no dado')
    sleep(1)

ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
# Aqui foi importada a função itemgetter que vai nos dizer através de onde a gente quer organizar o dict
# se queremos organizar ele no tempo 0 (que são as keys) ou no tempo 1 (que são os values)
# por ele colocar em ordem crescente, o reverse serve pra colocar na decrescente

print()
for contador, value in enumerate(ranking):
    print(f'{contador+1}º lugar para {value[0]} com {value[1]} pontos')
#quando copiamos os valores do dicionaria para a lista as keys tbm se tornaram valores dentro da lista
#juntamento os values (numero aleatorios). Desta forma foi possivel chamar a key por value[0] e o value por value[1]

