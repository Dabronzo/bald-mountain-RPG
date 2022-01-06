import json

# Global Varibles
visited_tabern = False
visited_inn = False
change_inn = False


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
        print(f"{self.name} got {self.damage} of damage")
        print(f"{self.name} health now is {self.health}")


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
    def __init__(self, input_name):
        self.input_name = input_name
        Entity.__init__(self, self.input_name, 100)

    inventory = {}

    def add_to_inventory(self, item, damage):
        self.inventory[item] = damage
        print(f"***A {item} was added to yout inventory***\n")

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
            raise ValueError("Invalid input.. must be an 'N' or 'n'")
    except ValueError:
        print(f"{input} is an invalid answer, try again")


def the_cave_two():
    """
    Function for the second part of the cave
    """
    global change_inn
    cave_two_data = data_extractor()
    main_text = cave_two_data["cave_second"]
    dash_line = cave_two_data["division_line"]
    print(dash_line)
    print(main_text)
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
            print(dash_line)
            print('The fight is over')
            if enemy01.health <= 0:
                del enemy01
                player.get_status()
                change_inn = True
                main_road()
            else:
                game_over()


def the_cave_one():
    """
    Function for the first part of the cave
    """
    cave_one_data = data_extractor()
    entrance = cave_one_data["cave_first"]
    dash_line = cave_one_data["division_line"]
    print(entrance)
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
            print(dash_line)
            print('The fight is over')
            if enemy01.health <= 0:
                del enemy01
                player.get_status()
                the_cave_two()
            else:
                game_over()
        else:
            print(dash_line)
            print("You don't have a sword to fight!!")
            print("Going back to the main road")
            print(dash_line)
            main_road()
    else:
        print("you ran away")


def the_mountain():
    """
    Function to process the mountain stage of the game
    """
    mountain_data = data_extractor()
    first_part = mountain_data["mountain_begin"]
    middle_part = mountain_data["mountain_middle"]
    dash_line = mountain_data["division_line"]
    print(dash_line)
    print("You are now on the way to the mountain.\n")
    print(first_part)
    while True:
        action = input("Do you want to proceed? type 'Y' or 'N'\n")
        if validate_yes_no(action):
            break
    if validate_yes_no(action) == 'yes':
        print(dash_line)
        print(middle_part)
        final_fight()
    else:
        print(dash_line)
        print("You are going back to the main road")
        main_road()


def final_fight():
    """
    Function to handle the final fight of the game
    """
    data = data_extractor()
    dash_line = data["division_line"]

    input("Enter any key to continue...\n")

    troll = Enemy('troll', 'sword', 20)
    print(dash_line)
    print("The final fight")
    if player.inventory.get('sword'):
        while True:
            if fight(player, troll):
                break
    else:
        print("You didn't have a sword")
        print("The Troll easily killed you")
        game_over()


def game_over():
    """
    Function to handle the game over
    """
    print('----------------------------------------------------------------')
    print("Sorry, you have lost the game...")


def fight(player, enemy):
    while True:
        print(f"{player.name} attacks {enemy.name}")
        enemy.take_hit(player.get_the_damage())
        if enemy.health <= 0:
            break
        print(f"{enemy.name} attacks {player.name}")
        player.take_hit(enemy.get_enemy_damage())
        if player.health <= 0:
            break
    return True


def the_inn():
    """
    Functions for the events on the Inn scenario
    """
    global visited_inn
    inn_data = data_extractor()
    first_time = inn_data["first_inn"]
    inn_keeper = inn_data["inn_keeper"]
    second_time = inn_data["second_inn"]
    third_time = inn_data["third_inn"]
    dash_line = inn_data["division_line"]
    print(dash_line)
    print("You are now at the Inn...\n")
    if change_inn:
        print(dash_line)
        print(third_time)
        while True:
            action = input("Do you will take a rest? type 'Y' or 'N'\n")
            if validate_yes_no(action):
                break
        if validate_yes_no(action) == 'yes':
            print("Your health is fully restored")
            player.health = 100
        else:
            print(dash_line)
            print("You'll be back on the town")
            the_town()
    if visited_inn is False:
        print(first_time)
        print(inn_keeper)
        player.add_to_inventory('sword', 30)
        print(dash_line)
    elif visited_inn and not change_inn:
        print(second_time)
        print(dash_line)
    elif visited_inn and change_inn:
        print(third_time)
        print(dash_line)
    while True:
        print("Seams that you have nothing else to do here...")
        input("Press any key to go back to the village center\n")
        break
    visited_inn = True
    the_town()


def data_extractor():
    """
    Function to open the data file json and return it
    """
    with open("data.json") as data:
        json_data = json.load(data)
        data.close()
        return json_data


def the_tavern():
    """
    Function to handle the actions inside the tavern at the village
    """
    global visited_tabern
    tavern_data = data_extractor()
    line_dash = tavern_data['division_line']
    first_sentences = tavern_data['fist_time_tavern']
    old_man = tavern_data['old_man']
    torch_text = tavern_data['torch']
    second_time = tavern_data['second_time_tavern']
    print(line_dash)
    print("You are entering the Tavern...\n")
    if visited_tabern is False:
        print(line_dash)
        print(first_sentences)
        print(old_man)
        print(torch_text)
        player.add_to_inventory('torch', 1)
        print(line_dash)
        visited_tabern = True
    else:
        print(second_time)
        print(line_dash)
    while True:
        print("Seams that you have nothing else to do here...\n")
        input("Press any key to left go back to the village center\n")
        break
    the_town()


def the_town():
    """
    Functions that runs the town scenario
    """
    town_data = data_extractor()
    dash_line = town_data["division_line"]
    main_message = town_data["town_main"]
    option_tavern = town_data["tavern_option"]
    option_inn = town_data["inn_option"]
    option_exit = town_data["exit_option"]
    print(dash_line)
    print("You are now at the village.\n")
    print(main_message)
    print(option_tavern)
    print(option_inn)
    print(option_exit)

    while True:
        action = input("Type here your next action: \n")
        if validate_action_town(action):
            break
    action_handler_town(validate_action_town(action))


def the_cave():
    """
    Function that runs the cave senario
    """
    cave_data = data_extractor()
    dash_line = cave_data["division_line"]
    cave_entrance = cave_data["cave_entrance"]
    proceed = cave_data["proceed_yes_no"]
    print(dash_line)
    print(cave_entrance)
    action = input(proceed)
    if action == 'Y' or action == 'y':
        if(player.inventory.get('torch')):
            print(dash_line)
            print('you are entering the cave\n')
            the_cave_one()
        else:
            print(dash_line)
            print('You can not porceed without a torch.\n')
            print('Going back to the main road...')
            main_road()
    else:
        print('Going back to the main road...\n')
        main_road()


def main_road():
    """
    When called bring the player to the main road where
    can be decided where to go next with the three options
    """
    road_data = data_extractor()
    entrance = road_data["main_road"]
    dash_line = road_data["division_line"]
    option_cave = road_data["cave_option"]
    option_village = road_data["village_option"]
    option_mountain = road_data["mountain_option"]

    print(dash_line)
    print("...Main Road...\n")
    print(entrance)
    print(option_cave)
    print(option_village)
    print(option_mountain)

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

def start_game():
    """
    Start game function that will print the introduction of the game
    and calls the main_road function.
    """
    history = data_extractor()
    greetings = history["game_greetings"]
    prologue = history["game_prologue"]
    dash_line = history["division_line"]
    
    print(dash_line)
    print(greetings)
    print(prologue)
    print(dash_line)
    action = input("Enter any key to continue...\n")
    if action is not None:
        main_road()


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


name_player = input("To start the game please enter your name: ")

player = Player(name_player)
player.get_status()
player.add_to_inventory('sword', 40)
#start_game()

enemy = Enemy('troll', 'sword', 20)
fight(player, enemy)

