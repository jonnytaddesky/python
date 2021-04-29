players = {
    'Carlsen': 2842,
    'Caruana': 2822,
    'Mamedyarov': 2801,
    'Ding': 2797,
    'Giri': 2780
}


players = dict(Carlsen=2842, Caruana=2822,
               Mamedyarov=2801, Ding=2797, Giri=2780)
print(players)

top1 = players['Carlsen']
print(f"Top chees player`s ratting is {top1}")
print(players.get('Carlsen'))

players['So'] = 2780
print(players)

players['So'] = 2781
print(players)

del players['So']
print(players)

keys = players.keys()
print(type(keys))
print(keys)

l = list(players.keys())
print(type(l))
print(l)

sorted(players.keys())

print('Carlsen' in players)
print('Kramnik' not in players)

vals = players.values()
print(type(vals))
print(vals)

vals = list(players.values())
print(type(vals))
print(vals)

sorted(players.values())

players_copy = players.copy()
print(players_copy)

for k, v in players.items():
    print(k, v)

items = players.items()
print(type(items))
print(items)

players.pop('Giri')
print(players)

print(players.popitem())
print(players)

print(len(players))

players.setdefault('Karjakin')
print(players)
