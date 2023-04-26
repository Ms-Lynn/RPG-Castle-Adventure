###############################################################################
# Title: Simple Text Adventure Game
# coder: Ms. Lynn
# version: 001
###############################################################################
''' Program creates a simple map using nested lists that a character
    can move around on through a simple menu.
'''
#------------------------------------------------------------------------------
# Current Location
row = 0                   
col = 0
max_row = 3
max_col = 2

# Continuous play variables
playing = True

# Nested lists (an array) are used to make a map. map[row][col]
map = [
     ["Start", "EmptySpace", "SpookySpace"],
     ["EmptySpace", "SpookySpace", "EmptySpace"],
     ["SpookySpace", "Treasure", "EmptySpace"],
     ["EmptySpace", "EmptySpace", "Key"]
 ]


# Functions -------------------------------------------------------------------
def Movement():
    """Function is a sub menu that controls the users movement in the game."""
    global row, col, max_row, max_col, playing
    while True:
        # Print only valid direction options to the consol.
        print(f"Choose a direction: ")
        if not row==0:
            print(f"-North")
        if not row==max_row:
            print(f"-South")
        if not col==max_col:
            print(f"-East")
        if not col==0:
            print(f"-West")
        dirchoice = input(f"Choice: ")
        # Test if input is valid and in bounds; then update players location.
        if dirchoice == "North" and row > 0:
            row -= 1
            break
        elif dirchoice == "South" and row < max_row:
            row += 1
            break
        elif dirchoice == "East" and col < max_col:
            col += 1
            break
        elif dirchoice == "West" and col > 0:
            col -= 1
            break
        elif dirchoice == "Quit":
            playing = False
            break
        else:
            print(f"Sorry you can not move that direction.")


# Main Code --------------------------------------------------------------------
# Game Introduction:
print(f"Welcome to my Castle!")
print(f"Please tour around, and when your ready to leave type 'Quit'.")
# Continuous Playing Loop:
while playing:
    location_description =  map[row][col]
    # Print a description of the players current room
    if location_description == "Start":
        print(f"You are in the starting position in a grand foyer.")
    elif location_description == "EmptySpace":
        print(f"Nothing but cobwebs in this room.")
    elif location_description == "SpookySpace":
        print(f"This room is very spooky, you better leave quickly!")
    elif location_description == "Treasure":
        print(f"There is a giant treasure chest in the middle of this room!")
    elif location_description == "Key":
        print(f"There is a key hanging on the wall in this room!")
    else:
        print(f"Unexpected error has occured, your location is unknown.")
    # Only option right now is to move about the castle.
    Movement()
# End Game:
print(f"Thanks for playing!!!!\n\n\n")