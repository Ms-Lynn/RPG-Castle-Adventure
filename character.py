##############################################################################
# Module: character
##############################################################################
''' All of the information on the players character. '''
##############################################################################

class Character:
    ''' Parent Class - character/player in the game. '''
  
    def __init__(player, name):
        player.name = name
        player.row = 0  # current players row location on map
        player.col = 0  # current players columb location on map
        # Empty list to use as inventory for to store items. 
        player.inventory = []

  
    def player_inventory(player, item):
        player.inventory.append(item)
        print(f"You have successfully added a {item} to your inventory.")


    def view_inventory(player):
        '''This function will print out the players inventory. '''
        if player.inventory:
          print("Supplies currently in your Inventory: ")
        for item in player.inventory:
            print(f" - {item}")
        else:
            print(f"{player.name} your Inventory is currently empty. ")

