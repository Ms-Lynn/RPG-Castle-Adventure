##############################################################################
# Title: RPG: Castle Adventure!
# Class: Computer Science 30
# coder: Ms. Lynn
# last updated: March 22nd, 2023
# version: 005
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
import random
import map

# Global Variables -----------------------------------------------------------
# Messages that will be reused through the game in a dictionary
messages = { "Quit" : "Thank for playing!'\n'You have now quit the game. ",
             "Error" : "Invalid choice, please make another selection. "}

row = 0     # current players row location on map
col = 0     # current players columb location on map

# Main Menu choices
main_menu = ["walk", "look"]
# Directions choices for a sub menu
direction_menu = ["north", "south", "east", "west"]

inventory = []  # empty list to use as inventory for objects 
# Database for object information
objects = {
          "Chest" : {"Description" : "You find a treasure chest.",
                     "Status" : "closed",
                     "Location": [2, 1], 
                     "Action" : ["open","inspect", "done"],
                     "Requirement" : ["key", None, None]
                    },
          "Key" : {"Description" : "You find a key haning on the wall.",
                   "Status" : "lost",
                   "Location" : [0, 1],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  }, 
          "Treasure" : {"Description" : "You found some.",
                   "Status" : "in chest",
                   "Location" : [None, None],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  }
          }


# Functions ------------------------------------------------------------------
def SetUpGame():
    '''Function is used to set up the game. This function will "hide"
       the key object by placing it in a random room.'''
    global objects
    row_list = []
    for i in range(0, (int(map.max_row)+1), 1):
        row_list.append(i)
    objects["Key"]["Location"][0] = random.choice(row_list)
    col_list = []
    for j in range(0, (int(map.max_col)+1), 1):
        col_list.append(j)
    objects["Key"]["Location"][1] = random.choice(col_list)
    #x = objects["Key"]["Location"][0]
    #y = objects["Key"]["Location"][1]
    #print(f"Test {x}, {y}")

def Movement():
    '''When player choosed 'walk' in the main menu it trigers this
       movement functions. This function will have a sub menu of
       directions for the user to choose from. When a valid choice
       is made the global variables row and col[umb] will be changed
       so that the players current location will update.'''
    global row, col, messages, direction_menu
    orientating = True
    while orientating:
        print(f"   Choose a direction: ")
        if not row==0:
            print(f"   -{direction_menu[0].capitalize()}")
        if not row==map.max_row:
            print(f"   -{direction_menu[1].capitalize()}")
        if not col==map.max_col:
            print(f"   -{direction_menu[2].capitalize()}")
        if not col==0:
            print(f"   -{direction_menu[3].capitalize()}")
        orientating = False
        dirchoice = input(f"   Choice: ").lower()
        if dirchoice == direction_menu[0] and row > 0:
            row -= 1
        elif dirchoice == direction_menu[1] and row < map.max_row:
            row += 1
        elif dirchoice == direction_menu[2] and col < map.max_col:
            col += 1
        elif dirchoice == direction_menu[3] and col > 0:
            col -= 1
        elif dirchoice == "quit":
            print(f"{messages['Quit']} ")
            sys.exit()
        else:
            print(f"{messages['Error']}")
            orientating = True


def InspectRoom():
    '''When player choosed 'look' in the main menu it trigers this
       inspect room functions. This function will look through the 
       games object and see if any are located on the players current
       tile. If one is then a sub menu will populate from that object
       dictionary.'''
    global row, col, inventory, objects
    found_object = False
    room_inventory = []
    location_description =  map.map[row][col]
    print(f"You look around the room.")
    for object in objects:
        object_row = objects[object]["Location"][0]
        object_col = objects[object]["Location"][1]
        if object_row == row and object_col == col:
            print(f"{objects[object]['Description']}")
            found_object = True
            room_inventory.append(object)
    if found_object == True:
        for item in room_inventory:
            if item == "Chest":
                ChestActions()
            elif item == "Key":
                KeyActions()
            else:
                print(f"There are no interactive objects in this room.")
    else:
        print(f"There are no objects in this room.")
    room_inventory = []


def MainMenu():
    '''When the game is activated these are all the players inital
       actions that are possible. This is the games main menu.'''
    global messages
    thinking = True
    while thinking:
        print(f"   Choose to move to another room or look around: ")
        # loop through all main menu options and print to the screen
        for options in main_menu:
            print(f"   -{options.capitalize()}")
        mainChoice = input(f"   Choice: ").lower()
        if mainChoice == "walk":
            Movement()
            thinking = False
        elif mainChoice == "look":
            InspectRoom()
            thinking = False
        elif mainChoice == "quit":
            print(f"{messages['Quit']} ")
            sys.exit()
        else:
            print(f"{messages['Error']}") 


def TreasureActions():
  '''When the player looks inside a full chest this function is triggered.
     This function will allow for the player to take the treasure and win the
     game. Player can not get out of this loop without ending the game. '''
  global objects, inventory, messages
  # Loop will not end until the game does. Take the Treasure.
  while True:
      print(f"   Choose an Actions: ")
      for action in objects["Treasure"]["Action"]:
          print(f"   -{action.capitalize()}")
      gold_choice = input("   Actions: ").lower()
      # Take the Treasure and win the game! -------------------------
      if gold_choice == objects["Treasure"]["Action"][0]:
              objects["Treasure"]["Status"] = "in inventory"
              objects["Chest"]["Status"] = "open"
              objects["Treasure"]["Location"][0] = None
              objects["Treasure"]["Location"][1] = None
              inventory.append("Gold")
              print(f"\n\nCongrats you have won the game!\n")
              print(f"  Object Confirmations: ")
              for object in objects:
                  print(f"  - {object}'s Statue: {objects[object]['Status']}")
              print(f"  Inventory Confirmations: ")
              for item in inventory:
                  print(f"  - {item}")
              print(f"\nGame Over! Goodbye! \n\n\n ")
              sys.exit()
      elif gold_choice == objects["Treasure"]["Action"][1]:
          print(f"I don't think it is a good idea to leave the Gold behind.")
          print(f"Try again.")
      elif gold_choice == "quit":
          print(f"{messages['Quit']} ")
          sys.exit()
      else:
          print(f"{messages['Error']}")
          print(f"Try again.")
        

def ChestActions():
    '''When the player choosed to inspect the chest object this function
       is triggered so that it can provided valid options pertaining to this
       object. Main game play goal is to find a key and then open this chest.'''
    global objects, inventory, messages
    deciding = True
    while deciding:
        print(f"   Choose an Actions: ")
        for action in objects["Chest"]["Action"]:
            print(f"   -{action.capitalize()}")
        chest_choice = input("   Actions: ").lower()
        # Open the Treasure Chest--------------------------------------
        if chest_choice == objects["Chest"]["Action"][0]:  
            if objects["Chest"]["Status"] == "full":
                print(f"The cheat is already open but....") 
                print(f"...there is somthing shiny inside.")
            elif objects["Chest"]["Status"] == "open":
                print(f"The cheat is already open.")
            else:
                itemfound = False
                for item in inventory:
                    if item == objects["Chest"]["Requirement"][0]:
                        inventory.remove("key")
                        print(f"You opened the chest!")
                        print(f"You should look inside the chest.")
                        objects["Chest"]["Status"] = "full"
                        objects["Treasure"]["Location"][0] = row
                        objects["Treasure"]["Location"][1] = col
                        itemfound = True
                if itemfound == False:
                    print(f"You need to find a key to open the chest.")
        # Inspect the Treasure Chest--------------------------------------
        elif chest_choice == objects["Chest"]["Action"][1]: 
            if objects["Chest"]["Status"] == "closed":
                print(f"The chest appears to be locked.")
            elif objects["Chest"]["Status"] == "full":
                print(f"The chest has some gold in it.")
                TreasureActions()
            elif objects["Chest"]["Status"] == "open":
                print(f"The chest appears to be open.")
            else:
                print(f"Something has gone wrong with the chest.")
        elif chest_choice == objects["Chest"]["Action"][2]:
            deciding = False
        elif chest_choice == "quit":
            print(f"{messages['Quit']} ")
            sys.exit()
        else:
            print(f"{messages['Error']}")
  

def KeyActions():
    '''When the player finds the key object this fuction will trigger to give
       the player options that are unique to this object. The play will be able
       to pick up the key and place it in their inventory. '''
    global objects, inventory, messages
    deciding = True
    while deciding: 
        print(f"   Choose an Actions: ")
        for action in objects["Key"]["Action"]:
            print(f"   -{action.capitalize()}")
        key_choice = input("   Actions: ").lower()
        # Take Key  --------------------------------------
        if key_choice == objects["Key"]["Action"][0]:  
            objects["Key"]["Location"][0] = None
            objects["Key"]["Location"][1] = None
            objects["Key"]["Status"] = "found"
            print(f"Congrats the key is now in your inventory!")
            inventory.append("key")
            deciding = False
        elif key_choice == objects["Key"]["Action"][1]:
            print(f"You decided to leave the key alone.")
            deciding = False
        elif key_choice == "quit":
            print(f"{messages['Quit']} ")
            sys.exit()
        else:
            print(f"{messages['Error']}")
        
  
# Main -----------------------------------------------------------------------
print(f"Welcome to my Castle!\n")
print(f"Goal is to find and open a treasure chest.")
print(f"Type Quit at any time to quit the game.\n")
# Set us game by hiding the key on a random tile
SetUpGame()
while True:
    location_description =  map.map[row][col]
    for tile_option in map.tiles:
      if tile_option == location_description:
        print(f"{map.tiles[tile_option]['Description']}")
    MainMenu()