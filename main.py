##############################################################################
# Title: RPG: Castle Adventure!
# Class: Computer Science 30
# coder: Ms. Lynn
# last updated: May 5th, 2023
# version: 008
##############################################################################
''' Simple Text Adventure Game!

    Game takes place in a castle, created with a map.
    Player can choose to move around the map and to look around.
    Players goal is to find and open a treasure chest. Player wins when they
    take the gold from the treasure chest. In order to open the teasure chest 
    the player must find and take a key. Every time the game is started the 
    key will be placed in a randon room.
'''
##############################################################################
# Imports and Global Variables -----------------------------------------------
import sys
import message
from character import *

# Make a player one object with character class.
user = Character(None)

# Main Menu choices.
main_menu = {"explore": {"description": "Explore another room."},
             "search": {"description": "Search the room your currently in."}, 
        "map": {"description": "View a map of the castle."}, 
        "inventory": {"description": "View your current inventory."}
        }
# Directions choices for a sub menu.
directions = [["north", 'n'], ["south", 's'], ["east", 'e'], ["west", 'w']]


# Functions ------------------------------------------------------------------
def SetUpGame():
    '''This fuction will call all the the nessesary setup functions.'''
    pass #inventory.HideKey()    
    #map.ExportMap()


def MainMenu():
    '''When the game is activated these are all the players inital
       actions that are possible. This is the games main menu.
       player: is the current player playing the game.
    '''
    print("\nChoose one of the following options: ")
    # loop through all main menu options and print to the screen.
    for option in main_menu:
        print(f" - {main_menu[option]['description']} ({option})")
    choice = input("Choice: ").lower()
    # Check if the player wants to quit sys.exit() or any terminating command
    # will trigger an exception (with Replit) this is an uneligant solution.
    if choice == "quit" or choice == 'q':
        QuitGame()
    try:
        # Compare choices to the vaild options and their first char shortcuts.
        menu = list(main_menu.keys())
        if choice == menu[0] or choice == menu[0][0]: # explore
            pass#Movement()''''
        elif choice == menu[1] or choice == menu[1][0]: # search
            print("You found a sheild.")
            user.player_inventory("sheild")
            #inventory.InspectRoom()
        elif choice == menu[2] or choice == menu[2][0]: # map
            pass#map.ReadMap()
        elif choice == menu[3] or choice == menu[3][0]: # inventory
            user.view_inventory()
        elif choice == "cheat":
            pass#print(f"   Key Cheat: {inventory.items['Key']['Location']}")
        else:
            print(f"{message.messages['Error']}") 
    except:
        print(f"{message.messages['Exception']}")
    else:
        print(f"Keep up the good work {user.name}.")
    finally:
        print("Continue playing adventurer.")


def QuitGame():
    print(f"\n{message.messages['Quit']} ")
    sys.exit()


# Main -----------------------------------------------------------------------
# Change players one name to match the users.
user.name = (input("What is your name? "))
print(f"\nWelcome to my Castle {user.name}!\n")
print("Your goal is to find and open a treasure chest.")
print("You can type Quit at any time to quit the game.")
# Set us game by hiding the key on a random tile.
SetUpGame()

# Continuous game play loop.
while True:
    MainMenu() 
  