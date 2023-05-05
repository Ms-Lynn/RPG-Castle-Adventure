##############################################################################
# Title: RPG: Castle Adventure!
# Class: Computer Science 30
# coder: Ms. Lynn
# last updated: April 26, 2023
# version: 006
##############################################################################
''' Simple Text Adventure Game!

    Game takes place in a castle, created with a map.
    Player can choose to move around the map and to look around.
    Players goal is to find and open a treasure chest. Player wins when they
    take the gold from the treasure chest. In order to open the teasure chest 
    the player must find and take a key. Every time the game is started the 
    key will be placed in a randon room; this is possible because the program 
    imported a random library.

    The map is make with an array(nested lists). 
    Each Map item is a type of tile.
    Tile detalies are stored in a nested dictionary(database).
    Map information is now stored in a map.md module.

    Odjects characteristics and current statues are stored in a nested 
    dictionary(databases).
    Player has an inventory created by an empty list.
    Some objects can be picked up and added to the players inventory.

    Players can quit the game at anytime, the game will end using sys.exit()
    a funtion that is imported with the sys library.

    All of the players choices are confirmed by printing relivant messages to
    the consol. Lots of messages repeat so there is a dictionary of common
    messages that can be referenced and used throught the code.
'''
##############################################################################
# Imports --------------------------------------------------------------------
import sys
import map
import inventory
import character
import message

# Global Variables -----------------------------------------------------------
# Main Menu choices
main_menu = ["explore", "search", "view map", "view inventory"]
# Directions choices for a sub menu
direction_menu = ["north", "south", "east", "west"]


# Functions ------------------------------------------------------------------
def SetUpGame():
    '''This fuction will call all the the nessesary setup functions.'''
    inventory.HideKey()    
    map.ExportMap()


def Movement():
    '''When player choosed 'walk' in the main menu it trigers this
       movement functions. This function will have a sub menu of
       directions for the user to choose from. When a valid choice
       is made the global variables row and col[umb] will be changed
       so that the players current location will update.
    '''
    global direction_menu
    try:
      thinking = True
      while thinking:
          thinking = False
          print("   Choose a direction: ")
          # Only print valid direction choices based on players location.
          if not character.row==0:
              print(f"   -{direction_menu[0].capitalize()}")
          if not character.row==map.max_row:
              print(f"   -{direction_menu[1].capitalize()}")
          if not character.col==map.max_col:
              print(f"   -{direction_menu[2].capitalize()}")
          if not character.col==0:
              print(f"   -{direction_menu[3].capitalize()}")
          # Get the users direction choice.
          dirchoice = input("   Choice: ").lower()
          if dirchoice == direction_menu[0] and character.row > 0:
              character.row -= 1
          elif dirchoice == direction_menu[1] and character.row < map.max_row:
              character.row += 1
          elif dirchoice == direction_menu[2] and character.col < map.max_col:
              character.col += 1
          elif dirchoice == direction_menu[3] and character.col > 0:
              character.col -= 1
          elif dirchoice == "quit":
              print(f"\n{message.messages['Quit']} ")
              sys.exit()
          else:
              print(f"   {message.messages['Error']}")
              thinking = True # Repeat
    except SystemExit:
        print("In games and in life:")
        sys.exit()
    except:
        print(f"   {message.messages['Exception']}")
    else:
        print(f"You successfully moved {dirchoice}.")
    finally:
        # Message will always print even when quitting.
        print("Continue exploring adventurer.")      


def MainMenu():
    '''When the game is activated these are all the players inital
       actions that are possible. This is the games main menu.
    '''
    try:
        print("   Choose one of the following options: ")
        # loop through all main menu options and print to the screen
        for options in main_menu:
            print(f"   -{options.capitalize()}")
        mainChoice = input("   Choice: ").lower()
        if mainChoice == main_menu[0]: # walk
            Movement()
        elif mainChoice == main_menu[1]: # look
            inventory.InspectRoom()
        elif mainChoice == main_menu[2]: # view map
            map.ReadMap()
        elif mainChoice == main_menu[3]: # view inventory
            inventory.ViewInventory()
        elif mainChoice == "cheat":
            print(f"   Key Cheat: {inventory.items['Key']['Location']}")
        elif mainChoice == "quit":
            print(f"\n{message.messages['Quit']} ")
            raise SystemExit()
        else:
            print(f"   {message.messages['Error']}") 
    except SystemExit: # Handle Replits Exit Error
        sys.exit()
    except:
        print(f"{message.messages['Exception']}")
    else:
        pass
    finally:
        pass


# Main -----------------------------------------------------------------------
print("Welcome to my Castle!\n")
print("Your goal is to find and open a treasure chest.")
print("You can type Quit at any time to quit the game.\n")
# Set us game by hiding the key on a random tile.
SetUpGame()
# Continuous Game Loop
while True:
    location_description =  map.map[character.row][character.col]
    for tile_option in map.tiles:
        if tile_option == location_description:
            print(f"\n{map.tiles[tile_option]['Description']}")
    MainMenu()  

