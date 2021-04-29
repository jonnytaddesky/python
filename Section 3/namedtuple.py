
from collections import namedtuple
players = [('Carlsen', 1990, 2842), ('Caruana', 1992, 2822),
           ('Mamedyarov', 1985, 2801)]
print(players[0])


# players[0].name


Player = namedtuple('Player', 'name age rating')


players = [Player('Carlsen', 1990, 2842), Player(
    'Caruana', 1992, 2822), Player('Mamedyarov', 1985, 2801)]


print(players[0])


print(players[0].name)


p1 = Player('Carlsen', 1990, 2842)


print(p1.name)
print(p1.age)
print(p1.rating)
