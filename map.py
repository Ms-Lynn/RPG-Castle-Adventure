##############################################################################
# Module: map
##############################################################################
''' All of the information for the game board '''
##############################################################################
from tabulate import tabulate
import message

# tile information
tile = ["Foyer", "Corridor", "Thrown Room", "Bedroom","Dinning Hall",
        "Ballroom", "Kitchen", "Dungeon", "Master Bedroom"]
tiles = {
    tile[0] : {"Description" : "You're in the foyer of a castle."},
    tile[1] : {"Description" : "You're are in a boring corridor."},
    tile[2] : {"Description" : "You're in a beautifly thrown room."},
    tile[3] : {"Description" : "You're is a very spooky bedroom!"},  
    tile[4] : {"Description" : "You're in the grand dinning hall!"}, 
    tile[5] : {"Description" : "You're in the haunted ballroom!"}, 
    tile[6] : {"Description" : "You're in a deserted kitchen!"}, 
    tile[7] : {"Description" : "You're in a haunted dungeon!"}, 
    tile[8] : {"Description" : "You're in the master bedroom."}
    }

# games map made with an array
map = [
      [tile[0], tile[1], tile[7]],
      [tile[1], tile[5], tile[1]],
      [tile[4], tile[2], tile[3]],
      [tile[6], tile[1], tile[3]]     
      ]

# map size
max_row = 3
max_col = 2

# maps external filename
mapfile = 'map.txt'


# Create an external file if the map
def ExportMap():
    '''Function will write the map to an external file. '''
    try:
        with open(mapfile, 'w') as file:
            file.write(tabulate(map,tablefmt = 'fancy_grid'))
    except:
        print(f"{message.messages['Write File']} ")
    else:
        print("You have been provided a map of the castle.")
        #print("Map printed to a file sucessfully.")
    finally:
        print("Though I'm note sure a map will help you survive.")


# Print out the map
def ReadMap():
    '''Function will read an external file to print a map to the consol. '''
    try:
        with open(mapfile, 'r') as file:
            print(file.read())
    except:
        print(f"{message.messages['Read File']} ")
    else:
        print("Good luck Adventurer.")
    finally:
        print("To bad the map didn't show you where ghost may be hidding.")