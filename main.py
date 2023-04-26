###############################################################################
# Title: Simple Text Adventure Game
# coder: Ms. Lynn
# version: 002
###############################################################################
''' Program creates a simple map using nested lists that a character
    can move around on through a simple menu.
    Character now has an inventory to collect 'objects' in.
    Program has two objects a key and a treasure chest.
    The key must be in the characters inventory in order to open the chest'''
#------------------------------------------------------------------------------
# Current Location
row = 0
col = 0
max_row = 3
max_col = 2

inventory = []

playing = True

chest = "closed"
key = "lost"

map = [
     ["Start", "EmptySpace", "SpookySpace"],
     ["EmptySpace", "EmptySpace", "EmptySpace"],
     ["SpookySpace", "Treasure", "EmptySpace"],
     ["EmptySpace", "EmptySpace", "Key"]
 ]

# Functions -------------------------------------------------------------------
def Movement():
    global row, col, max_row, max_col
    while True:
        print(f"Choose a direction: {row}, {col}")
        if not row==0:
            print(f"-North")
        if not row==max_row:
            print(f"-South")
        if not col==max_col:
            print(f"-East")
        if not col==0:
            print(f"-West")
        dirchoice = input(f"Choice: ")
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
        else:
            print(f"Sorry you can not move that direction.")

def FoundTreasure():
  global inventory, playing, chest
  thinking = True
  while thinking:
    print(f"Would you like to inspect the chest or leave the room?")
    print(f"-Inspect")
    print(f"-Leave")
    choice = input(f"Choice: ")
    if choice == "Inspect":
        print(f"The chest appears to be locked.")
        answering = True
        while answering:
            print("Whould you like to try and open it?")
            print(f"-Yes")
            print(f"-No")
            answer = input(f"Answer: ")
            if answer == "Yes":
                for item in inventory:
                    if item == "Key":
                        chest = "open"
                        print(f"Congrats your key opened the Chest!!!!")
                        playing = False
                        answering = False
                        thinking = False
                if chest == "closed":
                  print(f"You can not open the Treasure Chest.")
            elif answer == "No":
                Movement()
                answering = False
                thinking = False
            else:
                print(f"Sorry that is not an option.")
    elif choice == "Leave":
        thinking = False
        Movement()
    else:
        print(f"Sorry that is not an option.")


def FoundKey():
    global map
    while True:
        print(f"Would you like to pick up the key or leave?")
        print(f"-Leave")
        print(f"-Take")
        decition = input(f"Choise: ")
        if decition == "Leave":
            Movement()
            break
        elif decition == "Take":
            inventory.append("Key")
            map[row][col] = "EmptySpace"
            print(f"You now have a Key!")
            Movement()
            break
        else:
            print(f"Sorry that is not a valid option.")

# Main Code --------------------------------------------------------------------
while playing:
    location_description =  map[row][col]
    if location_description == "Start":
      print(f"Welcome to my Castle!")
      print(f"If you want to escape find and open my treasure chest.")
      Movement()
    elif location_description == "EmptySpace":
      print(f"Nothing is in this room.")
      Movement()
    elif location_description == "SpookySpace":
      print(f"This room is very spooky, you better leave quickly!")
      Movement()
    elif location_description == "Treasure":
      if chest == "closed":
          print(f"There is a giant treasure chest in the middle of the room!")
      else:
          print(f"There is an open treasure chest in this room!")
      FoundTreasure()
    elif location_description == "Key":
        print(f"There is a key hanging on the wall!")
        FoundKey()
print(f"Thanks for playing!!!!")
