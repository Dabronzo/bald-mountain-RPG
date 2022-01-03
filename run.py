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

def main_road():
    """
    When called bring the player to the main road where can be decided wher to go next
    with the three options
    """
    print("You are in a main road, you only see three possible ways to proceed. Where you would like to go?\n")
    print("The Cave -------- to go there type 'C'")
    print("The Town -------- to go there type 'T'")
    print("The Mountain ---- to go there type 'M'")
    
    direction = input("Type here where to go: \n")
    if direction == 'C' or direction == 'c':
        print('Oh no a goblin!!')
        enemy01 = Enemy('goblin', 'sword', 20)
        player.take_hit(enemy01.get_enemy_damage())


print("Welcome to the Bald Mountain RPG")
name_player = input("Please enter your name: ")

player = Player(name_player)
player.get_status()
main_road()