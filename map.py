##############################################################################
# Module: map
##############################################################################
'''
   All of the information for the game board
'''
##############################################################################
from tabulate import tabulate

edited = "test"

# tile information
tile = ["Foyer", "Corridor", "Thrown Room", "Bedroom", 
        "Dinning Hall", "Ballroom", "Kitchen", "Dungeon"]
tiles = {
    tile[0] : {"Description" : "You're in the foyer of a castle."},
    tile[1] : {"Description" : "You're are in a boring corridor."},
    tile[2] : {"Description" : "You're in a beautifly thrown room."},
    tile[3] : {"Description" : "You're is a very spooky bedroom!"},  
    tile[4] : {"Description" : "You're in the grand dinning hall!"}, 
    tile[5] : {"Description" : "You're in the haunted ballroom!"}, 
    tile[6] : {"Description" : "You're in a deserted kitchen!"}, 
    tile[7] : {"Description" : "You're in a haunted dungeon!"}, 
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
  with open(mapfile, 'w') as file:
    file.write(tabulate(map,tablefmt = 'fancy_grid'))

# Print out the map
def ReadMap():
  with open(mapfile, 'r') as file:
    print(file.read())