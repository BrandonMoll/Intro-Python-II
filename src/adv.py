from room import Room
from player import Player
from item import Item
import random

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

rooms_list = ['outside', 'foyer', 'overlook', 'narrow', 'treasure']
key_room = random.randint(0,4)
block_room = random.randint(0,4)
room[rooms_list[key_room]].items = [Item("Key")]
room[rooms_list[block_room]].items = [Item("Block")]

player_one = Player(room['outside'], [])
print("Welcome to the game!","\n")
print(str(rooms_list[key_room]), "and", str(rooms_list[block_room]))

selection = 0

def health():
    for x in player_one.items:
        if x.name == "Block":
            player_one.health -= 1

while selection != 'q':
    print("--------------------------------------", "\n")
    print(player_one)
    if len(player_one.current_room.items) > 0:
        print("To pick up an item, enter: pick up")
    selection = input("Which direction would you like to go? (N, E, S, W or Q to quit) ")
    
    try:
        selection = selection.lower().strip()
        if selection == 'n':
            health()
            player_one.current_room = player_one.current_room.n_to
        elif selection == 'e':
            health()
            player_one.current_room = player_one.current_room.e_to
        elif selection == 's':
            health()
            player_one.current_room = player_one.current_room.s_to
        elif selection == 'w':
            health()
            player_one.current_room = player_one.current_room.w_to
        elif len(player_one.current_room.items) > 0 and selection == "pick up":
            while True:
                i = 1
                for x in player_one.current_room.items:
                    output = ""
                    output += str(i) + ". " + x.name + "\n"
                print(output)
                item_selection = input("Enter the number for which Item you want to pick up: ")
                item_selection = int(item_selection)
                if item_selection > 0 and item_selection <= len(player_one.current_room.items):
                    item_name = player_one.current_room.items[item_selection-1]
                    if item_name == "Food":
                        player_one.health += 2
                        print("You have gained 2 health!")
                        break
                    else:
                        player_one.items = [Item(str(item_name))]
                        player_one.current_room.items.remove(item_name)
                        break
                else:
                    print("Please select a valid number")
        elif selection == 'q':
            print("Thank for playing!")
        else:
            print("--------------------------------------")
            print("***Please enter one of the 4 Cardinal directions***", "\n")
    except AttributeError:
        print("--------------------------------------")
        print("***There are no rooms in that direction, please select a different direction***", "\n")

