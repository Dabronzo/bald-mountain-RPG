import json


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
        print(f"The {self.name} got {self.damage} of damage")
        print(f"The {self.name} health now is {self.health}")

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
            Entity.__init__(self, 'troll', 100)
        self.weapons[weapon] = damage 
    def get_enemy_damage(self):
        return self.weapons.get('sword')
    def __del__(self):
        print(f"The {self.name} is dead")
     
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
        print(f"Player: {self.name} total health: {self.health}\n")

# Global Varibles
visited_tabern = False
visited_inn = False
change_inn = False

def validate_yes_no(input):
    """
    Function to validate the user input as yes or no type
    """
    try:
        if input == 'y' or input == 'Y':
            return 'yes'
        elif input == 'n' or input == 'N':
            return 'no'
        else:
            raise ValueError("The input is not aceptable.. must be an 'N' or 'n'")        
    except ValueError:
        print(f"{input} is an invalid answer, try again")

def the_cave_two():
    """
    Function for the second part of the cave
    """
    global change_inn
    print('----------------------------------------------------------------')
    print('You go deeper on the cave you hear more steps aproaching')
    print('Another goblin appears to attack you!')
    while True:
        action = input("Will you fight? type 'Y' or 'N\n")
        if validate_yes_no(action):
            break
    if validate_yes_no(action) == 'yes':
        if player.inventory.get('sword'):
            enemy01 = Enemy('goblin', 'sword', 20)
            while True:
                if fight(player, enemy01):
                    break
            print('----------------------------------------------------------------')
            print('The fight is over')
            del enemy01
            player.get_status()
            change_inn = True
            main_road()


def the_cave_one():
    """
    Function for the first part of the cave
    """
    print('----------------------------------------------------------------')
    print("As you enter the cave you notice an creature aproaching")
    print("It's a goblin, and it's going to attack you")
    while True:
        action = input("Will you fight? type 'Y' or 'N\n")
        if validate_yes_no(action):
            break
    if validate_yes_no(action) == 'yes':
        if player.inventory.get('sword'):
            enemy01 = Enemy('goblin', 'sword', 20)
            while True:
                if fight(player, enemy01):
                    break
            print('----------------------------------------------------------------')
            print('The fight is over')
            del enemy01
            player.get_status()
            the_cave_two()
        else:
            print('----------------------------------------------------------------')
            print("You don't have a sword to fight!!")
            print("Going back to the main road")
            print('----------------------------------------------------------------')
            main_road()
    else:
        print("you ran away")


def the_mountain():
    """
    Function to process the mountain stage of the game
    """
    print('----------------------------------------------------------------')
    print("You are now on the way to the mountain")
    print("You see a bunch of dead bodies and a dreadfull feeling about this place")
    while True:
        action = input("Do you want to proceed? type 'Y' or 'N'\n")
        if validate_yes_no(action):
            break
    if validate_yes_no(action) == 'yes':
        print('----------------------------------------------------------------')
        print("As you walk you hear a grunt aproaching")
        print("Before you can even think about it an enormous Troll aprear!")
        print("You can not run away this time. The fight will begin...")
        final_fight()
    else:
        print('----------------------------------------------------------------')
        print("You are going back to the main road")
        main_road()

def final_fight():
    """
    Function to handle the final fight of the game
    """
    troll = Enemy('troll', 'sword', 20)
    print('----------------------------------------------------------------')
    print("The final fight")
    if player.inventory.get('sword'):
        while True:
            if fight(player, troll):
                break
        print("You have finished the game")

def game_over():
    """
    Function to handle the game over
    """
    print('----------------------------------------------------------------')
    print("Sorry, you have lost the game...")



def fight(player, enemy):
    while True:
        enemy.take_hit(player.get_the_damage())
        if enemy.health <= 0:
            break
        player.take_hit(enemy.get_enemy_damage())
        if player.health <= 0:
            print("You are dead. Game Over")
            game_over()
            break
    return True

def the_inn():
    """
    Functions for the events on the Inn scenario
    """
    global visited_inn
    if change_inn:
        print('----------------------------------------------------------------')
        print("At the Inn")
        print("Hey, you look tired. I have a room avalible, do you want to take a rest?")
        while True:
            action = input("Do you will take a rest? type 'Y' or 'N'\n")
            if validate_yes_no(action):
                break
        if validate_yes_no(action) == 'yes':
            print("Your health is fully restored")
            player.health = 100
        else:
            print('----------------------------------------------------------------')
            print("You'll be back on the town")
            the_town()       
    if visited_inn is False:
        print('----------------------------------------------------------------')
        print("At the Inn")
        print("As you enter at the Inn you see a man at the reception, you aproach and he says:")
        print("Inn Keeper: Hello traveler, I shall warn you that we don't have more accommodations")
        print("Inn Keeper: Since that beast is at the mountain everybody who lives there flew away...")
        print("...and now they are here waiting for someone to kill the beast")
        print("You tell the man that you'll kill the beast")
        print("He laughts and take something behind his table")
        print("Inn Keeper:  Here you go, at leas take this sword with you...\n")
        print('----------------------------------------------------------------')
        player.add_to_inventory('sword', 30)
    elif visited_inn and not change_inn:
        print('----------------------------------------------------------------')
        print("At the Inn")
        print("Inn Keeper: Hello again, lost something?\n")
        print('----------------------------------------------------------------')
    elif visited_inn and change_inn:
        print('----------------------------------------------------------------')
        print("Inn Keeper: Hey you look better. Good luck today..\n")
        print('----------------------------------------------------------------')
    while True:
        print("Seams that you have nothing else to do here...")
        action = input("To go back to the Town type 'Y\n")

        if validate_yes_no(action):
            break
    visited_inn = True
    the_town()


def data_extractor():
    """
    Function to open the data file json and return it
    """
    with open("data.json") as data:
        jsonData = json.load(data)
        data.close()
        return jsonData

def the_tavern():
    """
    Function to handle the actions inside the tavern at the village
    """
    print("You are entering the Tavern...")
    global visited_tabern
    tavern_data = data_extractor()
    line_dash = tavern_data['division_line']
    first_sentences = tavern_data['fist_time_tavern']
    old_man = tavern_data['old_man']
    torch_text = tavern_data['torch']
    second_time = tavern_data['second_time_tavern']
    if visited_tabern is False:
        print(line_dash)
        print(first_sentences)
        print(old_man)
        print(torch_text)
        print(line_dash)
        player.add_to_inventory('torch', 1)
        visited_tabern = True
    else:
        print(line_dash)
        print(second_time)
    while True:
        print("Seams that you have nothing else to do here...")
        action = input("To go back to the Town type 'Y\n")

        if validate_yes_no(action):
            break
    the_town()
   

def the_town():
    """
    Functions that runs the town scenario
    """
    print('----------------------------------------------------------------')
    print("The town has a couple of buildings and a center, you only see two options to enter\n")
    print("The Tavern --------- to enter type 'T'")
    print("The Inn ------------ to enter type 'I'")
    print("Go back to the main road --- type 'E'\n")

    while True:
        action = input("Type here your next action: \n")
        if validate_action_town(action):
            break
    action_handler_town(validate_action_town(action))
    

def the_cave():
    """
    Function that runs the cave senario
    """
    print('----------------------------------------------------------------')
    print("You stop at the entrance. is dark and you can hear something further down on the cave")
    action = input("Do you want to proceed? type 'Y' for yes and 'N' for no.\n")
    if action == 'Y' or action == 'y':
        if(player.inventory.get('torch')):
            print('you are entering the cave')
            the_cave_one()
        else:
            print('----------------------------------------------------------------')
            print('you can not porceed without a torch')
            print('Going back to the main road...\n')
            print('----------------------------------------------------------------')
            main_road()
    else:
        print('Going back to the main road...\n')
        main_road()


def main_road():
    """
    When called bring the player to the main road where can be decided wher to go next
    with the three options
    """
    print('----------------------------------------------------------------')
    print("You are in a main road, you only see three possible ways to proceed. Where you would like to go?\n")
    print("The Cave -------- to go there type 'C'")
    print("The Village -------- to go there type 'V'")
    print("The Mountain ---- to go there type 'M'")

    while True:
        action = input("Type here your next action: \n")
        if validate_action_road(action):
            break
    action_handler_road(validate_action_road(action))

def validate_action_town(action):
    """
    Function to validate the user input on the town cenario
    """
    try:
        if action == 'T' or action == 't':
            return 'tavern'
        elif action == 'I' or action == 'i':
            return 'inn'
        elif action == 'E' or action == 'e':
            return 'exit'
        else:
            raise ValueError(f"The input value {action} is not valid")
    except ValueError:
        print(f"{action} is not valid, please try it again...")

def action_handler_town(action):
    """
    function that will validate and handle the user action in the Town
    """
    if action == 'tavern':
        the_tavern()
    elif action == 'inn':
        the_inn()
    elif action == 'exit':
        main_road()
       

def validate_action_road(action):
    """
    Function to validate the user input on the road stage
    """
    try:
        if action == 'C' or action == 'c':
            return 'cave'
        elif action == 'V' or action == 'v':
            return 'village'
        elif action == 'M' or action == 'm':
            return 'mountain'
        else:
            raise ValueError(f"The input data {action} is not valid!")
    except ValueError:
        print("An error happened due to invalid data, please try again..\n")



def action_handler_road(action):
    """
    function that will handle all the inputs of the user
    """
    if action == 'cave':
        the_cave()
    elif action == 'village':
        the_town()
    elif action == 'mountain':
        the_mountain()




print("Welcome to the Bald Mountain RPG")
name_player = input("Please enter your name: ")

player = Player(name_player)
player.get_status()
main_road()
