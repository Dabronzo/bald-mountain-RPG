# Bald Mountain RPG

Bald Mountain is a small RPG, made in Python to run in a terminal. I was inspired by the first generation of RPG games for computers where the player needed to type the decisions and actions on the screen in order to move(make progress?) in the game. The lack of any graphic stimulus as animation forces the player to use  imagination, as he reads the outcomes of his action on the screen.

### Current live version of the game: [Bald Mountain RPG](https://bald-mountain-rpg.herokuapp.com/)

## Table of Content
1. [**How to Play**](#how-to-play)

2. [**Technology Used**](#technology-used)

3. [**Flowchart**](#flowchart)

4. [**Features**](#features)
    * [**Open World**](#open-world)
    * [**Fight System**](#fight-system)
    * [**Non-Player Characters (NPC)**](#non-player-characters-npc)
    * [**User Inputs and Decisions**](#user-inputs-and-decisions)
    * [**Concept of Visited Areas**](#concept-of-visited-areas)
    * [**Inventory System**](#inventory-system)

5. [**Future Features**](#future-features)

6. [**Development**](#development)

7. [**Testing**](#testing)

8. [**Bugs**](#bugs)

9. [**Deployment**](#deployment)

10. [**Credits**](#credits)


## Live Version Exemple

![layout](/docs/lay_out.png)


## How to Play
 The game starts by asking your name. Then, all of your options are printed on the screen as you make decisions. You start on a main road which is near Bald Mountain. There’s three places to go: the mountain, the village and the cave. In order to choose one, the player needs to type a letter which will correspond to the place. Some characters at the locations may give the player items which will be stored in their inventory. In other places an item might be required in order to proceed. The fight happens automatically, the player always attacks first and then the enemy attacks, repeating until either the enemy or player dies. The status of the player’s health is printed on the screen after every fight which the player survives. The main objective of the player is to kill all of the creatures that are spreading fear and death into the mountain.

## Technology Used
- **Python** 
  - The language used to write the game
- **JSON**
  - Used as data files
- **Heroku**
  - Used for the deployment of the live version
- **GitHub**
  - Where the project repository is located
- **GitPod**
  - Used to write and develop the game as IDE
- **LucidCharts**
  - Used to make the flowchart. Link to their website: [LucidChart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier2_mixed_search_brand_exact_&km_CPC_CampaignId=1520850463&km_CPC_AdGroupID=57697288545&km_CPC_Keyword=lucidchart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433237648&km_CPC_TargetID=aud-381457345638:kwd-33511936169&km_CPC_Country=9065297&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAiA5t-OBhByEiwAhR-hmzeoUQEGtS1zTqvacTUBgPiaGTE6MdDiJyQd-4V6FSOfeReR53VxVhoCWpkQAvD_BwE)
- **Am I Responsive**
  - Used to show the layout of the live website. Link to their website: [Am I Rsponsive](http://ami.responsivedesign.is/)
- **External Content**
  - **Node.JS**
  - On the template provided by the **Code Institute**


## Flowchart

![flowchart](/docs/rpg_flowchart.png)
'*'  the two stages(functions) "main road" and "village" appear twice on the flowchart for a better display, the flow on code will bring the player back to the same functions, main road and village.
## Features
![start game](/docs/game_start.png)

### Open World
The idea is to bring a sense of an open world where the player can decide where to go at any time. Some places have a trigger event which will change the behavior of an NPC in the game, however the main idea is giving freedom to the player to make his own decision as to where to go first.

### Fight System
The fighting system of the game is quite peculiar. Once the fight starts the player gives the first strike and the enemy takes the damage, this repeats until one of the fighter’s health drops below or equal to zero. This means that all of the fights last until death, thus if the player loses the game is over. All of the fight stages are displayed on the screen so the player can follow the fight by seeing the whole fight log. After the fight, the player status is printed to let the user know how much health the character still has.

![fight](/docs/fight_sys.png)

### Non-Player Characters (NPC)
There are two types of enemies in the game: Goblins, located in the cave and have a total health of 40 and a sword which deals 20 of damage. The Troll is the boss of the game, it can be located on the mountain, and has a total health of 100 and also a sword that deals 20 of damage. The player will listen to two NPCs, an old man in the tavern who will give the player a torch and the innkeeper who will help the player with a sword.

### User Inputs and Decisions
- All the player interactions are made through input on the terminal. Sometimes the game will provide some options and the respective letters to them.
![open World](/docs/open_world_one.png)

- Other times, there will be a simple yes or no input order.
![yes or no](/docs/yes_no.png)

- That will provide the user some time to read the information without being lost on the terminal prints. Some inputs require no decisions to make and ask to type any key to continue.
![any key](/docs/any_key.png)

- All the input passes a validation. If the input does not match one of the options, it will keep the game in a loop by asking for the correct input until it is done.
![wrong](/docs/wrong_input.png)


### Concept of Visited Areas
The game has a logic system which can track the player if he has already visited some areas. That was made in order to avoid some bugs and possible inconsistency in the story. If you have been to the tavern before, the old man will not be there anymore and you’ll not get another torch and the same logic will happen in the inn.

![visited inn](/docs/second_inn.png)

Truth is that in this game you cannot defeat the troll at once. To succeed the player needs to finish the cave part first and get an armour. The armour will make the player suffer less damage; however, the player's health will be way too low to kill the troll. The right way is for the player to go back into the Inn after completing the cave scene because then he will be offered to take a rest. By doing it the player’s health will be restored and so the final fight will end with a victory.  

### Inventory System
A simple dictionary that hold the weapon as the key and the damage as the value. In case of the item being an armour the value is the resistance of the item. A method in-class add new item to the inventory whe called. 

**The items are automatically added to the player inventory along the game.**
![inventory](/docs/inventory.png)



## Future Features
- More enemies and places to the player go.
- More items and functionalities.
- A shield and block attack system.
- Allow the player to see the inventory.

## Development 
The game uses the class to create the enemies and the player, both are subclasses of the “Entity” class which holds the variable health and the method “take hit”. The player class has the inventory, his own damage system (to calculate the damage of the weapon) and a print status system. The Enemy class has a different damage system, when instantiating the weapon and the damage needed to be passed as arguments and also has a del method that prints a message when the enemy is eliminated.
- Functions Places
The “places” where the player can go are functions that print the texts for each of the scenes and additionally handles the decision making, for instance where to enter or go next. Other functions were made to help with different tasks. The functions of this type are: "the village", "main road", " the cave", "the mountain", "the tavern" and "the inn".
- Fight Function
akes the player and an enemy as argument, prints the fight log by calling the methods inside the classes and returns true when either the player’s or the enemy’s health goes to equal or below 0.

- Input validators and handlers
  - The function “validate action” verifies if the input given by the user matches the options available by a try method. There are two functions like that, one for the “main road” and other for “the village”.

  - The function “action handler” takes the validations from the previous functions and, according to the input call, reacts with the next action or a place where the player wants to go. There are two validate type functions: “the village” and “main road”.
  
- The Final Function
The final fight function, as the name suggests, will handle the final confrontation that the player should have in the game. The function verifies if the player has a sword and proceeds to create the troll and start the fight. If the player wins the “end game”, a function is called to congratulate the player and finish the game, in case that the player loses a “game over” function will be called instead.


- Data Extractor Function 
Most of the text that is printed during the game is stored in a json file called “data.json”, this function has the task to open, load and return the data so the other functions can call this function to access specific parts of the data during the game.

- Game Over Function
This function is called when the player dies, it prints a message asking if the player wants to play again by clicking on the “run” button above the terminal.

- End Game Function
Is called when the player defeats the Troll and finish the game, prints a final message and credits.

## Testing
TThe game has been tested manually during all of the development process on the local terminal and also on the **Heroku** hosting.
- No errors reported on **GitPod**
- Passed the code through a PEP8 linter and no issues were found
  - Pep8online website for testing http://pep8online.com/


## Bugs
- During the development it was noticed that even if the player dies at the final battle, the troll also would simultaneously. At this point, the player was getting confusing messages about whether the battle was won or lost. The problem was inside of the class enemy, I’ve created a method which is used to destroy the object and print a message. This way at the end of the fight, if the enemy health is zero or less the method is called, then the object is destroyed, and the message printed. When the player dies, the game stops, since the enemy class has the “del” method, when python calls it and some unexpected message is printed. To fix that an if statement was added. It checks if the enemy type is a troll, if true no message should be printed.

- ### Unsolved Bugs
  - There are no current unsolved bugs noticed


## Deployment
This project is deployed on **Heroku** using the **Code Institute's** mock terminal
- ### How to deploy
  - Fork or clone this repository
  - Using **Heroku** create a new app
  - Set the buildpacks tp **Python** and **Node.js** in this order
  - Link **Heroku** to the forked or cloned repository
  - Deploy 

## Credits
- Thanks to **Code Institute** for the template
- Thanks to my mentor **Brian O'Hare** for the insights and guidance.
- Thanks my partner at home on taking care of the house duties while I was developing this project.










