# Bald Mountain RPG

Bald Mountain is a small RPG made in Python to run in a terminal. I was inspired on the first generation of RPG games for computers where the player needed to type the decisions and actions on the screen to move on the game. The lack of any graphic or animation force the player to use the imagination as reads the outcomes on the screen.

## Deployment
To deployment of the live version was used **Heroku** linked to the repository in **GitHub**
### Current live version of the game: [Bald Mountain RPG](https://bald-mountain-rpg.herokuapp.com/)



## How to Play
 The game starts asking your name then all your options are printed on the screen as you take decisions. You start in a main road that is close to the Bald Mountain, you have three places to go: the mountain, the village and the cave. To do it so the player need to type a letter that correspond to the place to go. NPC may give the player items that will be stored in your inventory, some places require an item to allow the player to go.  The fight happens automatically, the player always attack first and then the enemy attacks, repeating until the enemy or player dies. After every fight if the player survives the status of the player’s health is printed on the screen. The main objective of the player is killing all the creatures that are spreading fear and death to the mountain.

## Tecnology Used
- **Python** 
- **JSON**
- **Heroku** for deployment

## Flowchart

![flowchart](/docs/rpg_flowchart.png)
'*' the two stages(functions) "main road" and "village" appears twice on the flowchart just for better display, on the code the flow will bring the player back to the same functions main road and village.
## Features
### Open World
The idea is to bring a sense of open world where the player decides where to go at any time. Some places have an trigger event that will change a behaviour of an NPC on the game but the main idea is the player free to make the decision to where go first.
### Fight System
The fighting system of the game is quite peculiar, when the fight starts the player gives the first strike and the enemy deals with the damage, this repeats until one of the fighter’s health drops equal or bellow zero. That means all the fights are until death so if the player loses is game over. All the stages of the fight are displayed on the screen so the player can see how was the fight log, and the player status is printed after the fight to let the user know how much the character still have on health.
### Enemies and NPC
There are two types of enemies on the game: Goblins, are located on the cave, they have a total health of 40 and a sword that deals 20 of damage. The Troll is the boss of the game, and can be located on the mountain, he has a total health of 100 and also a sword that deals 20 of damage. The player will listen two NPCs, an old man in the tavern that will give the player an torch and the inn keeper that will help the player with a sword.
### User Inputs and Decisions
- All the player interactions are made through input on the terminal, sometimes the game will provide a few options and the respective letters to them.

Image options

- Other times will be a simple yes or no input

Image yes or no

- In order give time to the user read and take process the information that the game prints some inputs were there is no decision it’s just to type any key to the game continue.

Image any key

- All the input passes for a validation where if the input does not match one of the options will keep the game in the loop asking for the correct input until is done.

Image Wrong inputs

### Concept of Visited Areas
The game has a logic system that can track if the player has already visited some area, this is made to avoid a few bugs and possible inconsistency on the story. If you have been on the tavern before the old man will not be there anymore and you’ll not get another torch, the same logic will happen on the inn.

Image on the Inn for the second time

The real thing on this game is that you cannot defeat the troll at once. After the fight on the cave the player will have only 60 of health and needs to fight the troll that has it full, 100, if the fight happens now the player will die. However, if the player goes back to the inn after finishing the cave the NPC there will say that there is a room available to the player take a rest. After the rest the player will have the health restored to 100 and now will be able to fight and win the troll.

### Inventory System
The player subclass has a dictionary that works as inventory. This allow the game to run the fight, once that the weapons and damages information are stored there, the game will search for specific items on the player’s inventory to allow enter in some places or even initiate a fight. 

The items are automatically added to the player inventory along the game.

Image of something being add to the inventory 


## Future Features
- More enemies and places to the player go
- More items and functionalities
- A shield and armour system
- Allow the player to see the inventory

## Development 
The game uses the class to create the enemies and the player, both are subclasses of the “Entity” class that holds the variable health and the method “take hit”. The player class has the inventory, his own damage system (to calculate the damage of the weapon) and a print status system. The Enemy class has a different damage system, when instantiated the weapon and the damage needed to be passed as arguments, also has a del method that print a message when the enemy is eliminated.
- Functions Places
The “places” where the player can go are functions that print the texts for each scene and also handles the decision making, where to enter or go next for instance. Other functions were made to help with other tasks. The functions of this type are: "the village", "main road", " the cave", "the mountain", "the tavern" and "the inn".
- Fight Function
Takes the player and an enemy as argument, prints the fight log by calling the methods inside the classes and return true when either the player or the enemy heath goes bellow or equal to 0.
- Input validators and handlers
  - The function “validate action” verify by a try method if the input given by the user matches the options available. There are two functions like that, one for the “main road” and for “the village”.

  - Function “action handler” takes the validations from the previous functions and according to the input call the next action or place that the player wants to go. As the validate type there are two functions for “the village” and “main road”.
  
- The Final Function
The final fight function as the name suggest will handle the final confront that the player should have on the game. The function verifies if the player has a sword and creates the troll and starts the fight. If the player wins the “end game” function is called to congratulate the player and finish the game, in case of the player loses will call the “game over” function instead.

- Data Extractor Function 
Most of the text that is printed during the game is stored in a json file called “data.json”, this function have the task to open, load and return the data so the other functions can print specific parts during the game.

- Game Over Function
This function is called when the player died, prints a message asking if the player wants to play again by clicking on the “run” button above the terminal.

- End Game Function
Is called when the player defeats the Troll and finish the game, prints a final message and credits.

## Testing
The game has been teste manually during all the development process on the local terminal and also on the Heroku hosting.
- Passed the code through a PEP8 linter and no issues were found
  - Pep8online website for testing http://pep8online.com/
- Invalid inputs will be handled in game within a loop until the validate function return true.

## Bugs

## Unsolved Bugs










