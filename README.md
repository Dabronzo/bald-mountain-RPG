# Bald Mountain RPG

Bald Mountain is a small RPG made in Python to run in a terminal. I was inspired on the first generation of RPG games for computers where the player needed to type the decisions and actions on the screen to move on the game. The lack of any graphic or animation force the player to use the imagination as reads the outcomes on the screen.

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
 The game starts asking your name then all your options are printed on the screen as you take decisions. You start in a main road that is close to the Bald Mountain, you have three places to go: the mountain, the village and the cave. To do it so the player need to type a letter that correspond to the place to go. Some characters may give the player items that will be stored in your inventory, some places require an item to allow the player to go.  The fight happens automatically, the player always attack first and then the enemy attacks, repeating until the enemy or player dies. After every fight if the player survives the status of the player’s health is printed on the screen. The main objective of the player is killing all the creatures that are spreading fear and death to the mountain.

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
'*' the two stages(functions) "main road" and "village" appears twice on the flowchart just for better display, on the code the flow will bring the player back to the same functions main road and village.
## Features
![start game](/docs/game_start.png)

### Open World
The idea is to bring a sense of open world where the player decides where to go at any time. Some places have an trigger event that will change a behaviour of an NPC on the game but the main idea is the player free to make the decision to where go first.

### Fight System
The fighting system of the game is quite peculiar, when the fight starts the player gives the first strike and the enemy deals with the damage, this repeats until one of the fighter’s health drops equal or bellow zero. That means all the fights are until death so if the player loses is game over. All the stages of the fight are displayed on the screen so the player can see how was the fight log, and the player status is printed after the fight to let the user know how much the character still have on health.
![fight](/docs/fight_sys.png)

### Non-Player Characters (NPC)
There are two types of enemies on the game: Goblins, are located on the cave, they have a total health of 40 and a sword that deals 20 of damage. The Troll is the boss of the game, and can be located on the mountain, he has a total health of 100 and also a sword that deals 20 of damage. The player will listen two NPCs, an old man in the tavern that will give the player an torch and the inn keeper that will help the player with a sword.

### User Inputs and Decisions
- All the player interactions are made through input on the terminal, sometimes the game will provide a few options and the respective letters to them.
![open World](/docs/open_world_one.png)

- Other times will be a simple yes or no input
![yes or no](/docs/yes_no.png)

- In order give time to the user read and take process the information that the game prints some inputs were there is no decision it’s just to type any key to continue.
![any key](/docs/any_key.png)

- All the input passes for a validation where if the input does not match one of the options will keep the game in the loop asking for the correct input until is done.
![wrong](/docs/wrong_input.png)


### Concept of Visited Areas
The game has a logic system that can track if the player has already visited some area, this is made to avoid a few bugs and possible inconsistency on the story. If you have been on the tavern before the old man will not be there anymore and you’ll not get another torch, the same logic will happen on the inn.

![visited inn](/docs/second_inn.png)

The real thing on this game is that you cannot defeat the troll at once. To do it so the player needs to finish the cave part and get an armour. The armour will make the player take less damage; however, the player health will be way too low to kill the troll. The way out is if the player goes back to the Inn after completed the cave and will be offered to take a rest. By doing it the player’s health will be restored so now the final fight will end with a victory.  

### Inventory System
The player subclass has a dictionary that works as inventory. This allow the game to run the fight, once that the weapons and damages information are stored there, the game will search for specific items on the player’s inventory to allow enter in some places or even initiate a fight. 

**The items are automatically added to the player inventory along the game.**
![inventory](/docs/inventory.png)



## Future Features
- More enemies and places to the player go
- More items and functionalities
- A shield and block attack system
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
- No errors reported on **GitPod**
- Passed the code through a PEP8 linter and no issues were found
  - Pep8online website for testing http://pep8online.com/


## Bugs
- During the develpment was noticed that even if the player dies at the final battle the troll also would die. At this point the player was getting confusing messages about if the battle was won or not. The problem was inside of the class enemy, I’ve created a method that used to destroy the object and print a message. This way when in the fight is over if the enemy health is zero or less the method is called, and the object is destroyed, and the message printed. When the player dies the game stops and the enemy type troll is destroyed by that, python destroy the object and because the class has the del method the game was printing the messages. To fix that was added an if statement that checks if the enemy type is troll, being true no message should be printed.

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










