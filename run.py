class Entity:
    """
    Base class for all the game entities
    """
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    def take_hit(self, damage):
        self.damage = damage
        self.health -= damage
        print(f"The {self.name} got {self.damage} of damage\n")
        print(f"The life now is {self.health}")

    

class Enemy(Entity):
    """
    Subclass of Entity for all the enemies of the game
    """
    weapons = {}
    def __init__(self, type, weapon, damage):
        self.type = type
        if self.type == 'goblin':
            Entity.__init__(self, 'goblin', 40)
        elif self.type == 'troll':
            Entity.__init__(self, 'troll', 80)
        self.weapons[weapon] = damage
    
    def get_enemy_damage(self):
        return self.weapons.get('sword')


       
class Player(Entity):
    """
    Subclass of Entity for the player
    """
    def __init__(self, inputName):
        self.inputName = inputName
        Entity.__init__(self, self.inputName, 100)
    
    inventory = {}

    def add_to_inventory(self, item, damage):
        self.inventory[item] = damage
        print(f"an {item} was added to yout inventory\n")

    def get_the_damage(self):
        if len(self.inventory) != 0:
            if 'sword' in self.inventory:
                return self.inventory.get('sword')
            else:
                print("You don't have a sword in yout inventory!")
        else:
            print("Your inventory is empty!")
    
    def get_status(self):
        print(f"Player: {self.name} Health: {self.health}\n")
