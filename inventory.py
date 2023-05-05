##############################################################################
# Module: objects
##############################################################################
''' All of the information for the games inventory and items in the game. '''
##############################################################################
import sys
import random
import map
import character
import message

# Empty list to use as inventory for to store items. 
inventory = []  

# Database for object information.
items = {
          "Key" : {"Description" : "You find a key haning on the wall.",
                   "Status" : "lost",
                   "Location" : [0, 1],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  }, 
          "Chest" : {"Description" : "You find a treasure chest.",
                     "Status" : "closed",
                     "Location": [2, 1], 
                     "Action" : ["open","inspect", "done"],
                     "Requirement" : ["key", None, None]
                    },
          "Treasure" : {"Description" : "You found some.",
                   "Status" : "in chest",
                   "Location" : [None, None],
                   "Action" : ["take", "leave"],
                   "Requirement" : [None, None]
                  }
          }


def HideKey():
    '''Function is used to set up the game. This function will "hide" the 
       key object by placing it in a random room.
    '''
    global items
    row_list = []
    for i in range(0, (int(map.max_row)+1), 1):
        row_list.append(i)
    items["Key"]["Location"][0] = random.choice(row_list)
    col_list = []
    for j in range(0, (int(map.max_col)+1), 1):
        col_list.append(j)
    items["Key"]["Location"][1] = random.choice(col_list)


def ViewInventory():
    '''This function will print out the players inventory. '''
    if inventory:
        print(f"   Inventory: ")
        for item in inventory:
            print(f"   -{item}")
    else:
        print("   Your inventory is empty.")
    print("You better not steal any of my things.")
  

def InspectRoom():
    '''When player choosed 'look' in the main menu it trigers this
       inspect room functions. This function will look through the 
       games object and see if any are located on the players current
       tile. If one is then a sub menu will populate from that object
       dictionary.
    '''
    global inventory, items
    found_object = False
    room_inventory = []
    location_description =  map.map[character.row][character.col]
    print(f"   You look around the room.")
    for object in items:
        object_row = items[object]["Location"][0]
        object_col = items[object]["Location"][1]
        if object_row == character.row and object_col == character.col:
            print(f"   {items[object]['Description']}")
            found_object = True
            room_inventory.append(object)
    if found_object == True:
        for item in room_inventory:
            if item == "Chest":
                ChestActions()
            elif item == "Key":
                KeyActions()
            else:
                print(f"   There are no interactive objects in this room.")
    else:
        print(f"   There are no objects in this room.")
    room_inventory = []


def TreasureActions():
  '''When the player looks inside a full chest this function is triggered.
     This function will allow for the player to take the treasure and win the
     game. Player can not get out of this loop without ending the game. 
  '''
  global items, inventory
  # Loop will not end until the game does. Take the Treasure.
  while True:
      try:
          print(f"   Choose an Actions: ")
          for action in items["Treasure"]["Action"]:
              print(f"   -{action.capitalize()}")
          gold_choice = input("   Actions: ").lower()
          # Take the Treasure and win the game!
          if gold_choice == items["Treasure"]["Action"][0]: # take
                  items["Treasure"]["Status"] = "in inventory"
                  items["Chest"]["Status"] = "open"
                  items["Treasure"]["Location"][0] = None
                  items["Treasure"]["Location"][1] = None
                  inventory.append("Gold")
                  print(f"\n\nCongrats you have won the game!\n")
                  print(f"Object Confirmations: ")
                  for object in items:
                      print(f"   -{object}'s Statue: "
                          + f"{items[object]['Status']}")
                  print(f"Inventory Confirmations: ")
                  for item in inventory:
                      print(f"   -{item}")
                  print(f"\nGame Over! Goodbye! \n\n\n ")
                  sys.exit()
          elif gold_choice == items["Treasure"]["Action"][1]: # leave
              print(f"   Are you sure you do not want to take the Gold.")
              print(f"   You already took and used a key that wasn't yours.")
          elif gold_choice == "quit":
              print(f"{message.messages['Quit']} ")
              sys.exit()
          else:
              print(f"{message.messages['Error']}")
              print(f"Try again.")
      except SystemExit: # Handle Replits Exit Error
          sys.exit()
      except:
          print(f"{message.messages['Exception']}")
      else:
          pass
      finally:
          pass
              

def ChestActions():
    '''When the player choosed to inspect the chest object this function
       is triggered so that it can provided valid options pertaining to this
       object. Main game play goal is to find a key and then open this chest.
    '''
    global items, inventory
    try:
        deciding = True
        while deciding:
            print(f"   Choose an Actions: ")
            for action in items["Chest"]["Action"]:
                print(f"   -{action.capitalize()}")
            chest_choice = input("   Actions: ").lower()
            # Open the Treasure Chest.
            if chest_choice == items["Chest"]["Action"][0]: # open 
                if items["Chest"]["Status"] == "full":
                    print(f"   The chest is already open but....") 
                    print(f"   ...there is somthing shiny inside.")
                elif items["Chest"]["Status"] == "open":
                    print(f"   The chest is already open.")
                else:
                    itemfound = False
                    for item in inventory:
                        if item == items["Chest"]["Requirement"][0]:
                            inventory.remove("key")
                            print(f"   You used the key you stole to open the"
                                + f"chest! \nDo you dare look inside??")
                            items["Chest"]["Status"] = "full"
                            items["Treasure"]["Location"][0] = character.row
                            items["Treasure"]["Location"][1] = character.col
                            itemfound = True
                    if itemfound == False:
                        print(f"You need to find a key to open the chest.")
            # Inspect the Treasure Chest.
            elif chest_choice == items["Chest"]["Action"][1]: # inspect
                if items["Chest"]["Status"] == "closed":
                    print(f"   The chest appears to be locked.")
                elif items["Chest"]["Status"] == "full":
                    print(f"   The chest has some gold in it.")
                    TreasureActions()
                elif items["Chest"]["Status"] == "open":
                    print(f"   The chest appears to be open.")
                else:
                    print(f"   Something has gone wrong with the chest.")
            elif chest_choice == items["Chest"]["Action"][2]: # done
                deciding = False
            elif chest_choice == "quit":
                print(f"{message.messages['Quit']} ")
                sys.exit()
            else:
                print(f"   {message.messages['Error']}")
                deciding = True # Repeat
    except SystemExit: # Handle Replits Exit Error
          sys.exit()
    except:
          print(f"   {message.messages['Exception']}")
    else:
        print("You might want to remember what room you found the Chest in.")
    finally:
        pass


def KeyActions():
    '''When the player finds the key object this fuction will trigger to give
       the player options that are unique to this object. The play will be able
       to pick up the key and place it in their inventory. 
    '''
    global items, inventory
    try: 
        deciding = True
        while deciding:
            deciding = False
            print(f"   Choose an Actions: ")
            for action in items["Key"]["Action"]:
                print(f"   -{action.capitalize()}")
            key_choice = input("   Actions: ").lower()
            # Take Key.
            if key_choice == items["Key"]["Action"][0]: # take  
                items["Key"]["Location"][0] = None
                items["Key"]["Location"][1] = None
                items["Key"]["Status"] = "found"
                print(f"   Congrats the key is now in your inventory!")
                inventory.append("key")
            elif key_choice == items["Key"]["Action"][1]: # leave
                print(f"   You decided to leave the key alone.")
            elif key_choice == "quit":
                print(f"{message.messages['Quit']} ")
                sys.exit()
            else:
                print(f"   {message.messages['Error']}")
                deciding = True # Repeat
    except SystemExit: # Handle Replits Exit Error
          sys.exit()
    except:
          print(f"{message.messages['Exception']}")
    else:
        print("You are a lucky adventurerer...or should I say tresspasser.")
    finally:
        print("I bet you don't even know how to use a key.")
        