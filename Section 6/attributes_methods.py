class Character():
    max_speed = 100
    dead_health = 0

    def __init__(self, race, damage=10, armor=20):
        self.race = race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage


    def is_dead(self):
        return self.health == Character.dead_health

unit = Character('Ork')

# unit.hit(20)
# print(unit.health)

# print(unit.is_dead())

# unit.hit(80)
# print(unit.is_dead())


# unit.health = -200
# print(unit.health)