class Character():

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor


unit = Character('Elf', 20, 40)
print(unit.race, unit.damage, unit.armor)
