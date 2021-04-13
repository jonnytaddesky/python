# lst = [1, 2, 3]
# print(repr(lst))
# print(lst)

# print(eval(repr(lst)) == lst)

# from datetime import datetime

# dt = datetime.now()
# print(repr(dt))
# print(dt)

class Character:
    def __init__(self, race, damage = 100):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f"Character('{self.race}', {self.damage})"

    def __str__(self):
        return f"{self.race} with damage = {self.damage}"

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False
    
    # def __ne__(self, other):
    #     pass


c = Character('Elf')
print(c)
d = eval(repr(c))
print(type(d))
print(d)
print(c == d)
print(c!=d)

