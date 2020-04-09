from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("The Cave Entrance",
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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Player creation

newPlayer = Player("Jeff Goldblum", "outside")

# item creation

rag = Item("dirty rag",
           f'that {newPlayer.name} uses for mysterious reasons')
lamp = Item("lamp", f'that allows {newPlayer.name} to illuminates dark places')
dagger = Item("dagger", f'that allows {newPlayer.name} to shank enemies')
child = Item(
    "small child", f'that {newPlayer.name} can throw at enemies')
poison = Item(
    "poison vial", f'to end {newPlayer.name}\'s existential suffering')

# initial item placement

newPlayer.add_item(rag)
room['foyer'].add_item(lamp)
room['overlook'].add_item(dagger)
room['narrow'].add_item(child)
room['treasure'].add_item(poison)

# starts game

update = print(
    f'{newPlayer.name} wakes up in {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')


direction_command = input(
    "Which way will you go? (n,s,e,w) Press i to view inventory or q to quit ")

while not direction_command == "q":
    if len(direction_command) > 1:
        if direction_command[0] == "drop":
            room[newPlayer.current_room].add_item(
                newPlayer.items[0])
            newPlayer.drop_item(newPlayer.items[0])
            print(f'You dropped a {direction_command[1]}!')
            direction_command = input(
                "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
        elif direction_command[0] == "take":
            if len(room[newPlayer.current_room].items) != 0:
                if direction_command[1] == room[newPlayer.current_room].items[0].name:
                    newPlayer.add_item(room[newPlayer.current_room].items[0])
                    room[newPlayer.current_room].drop_item(
                        room[newPlayer.current_room].items[0])
                    print(f'You took a {direction_command[1]}!')
                    direction_command = input(
                        "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
                else:
                    print('This item isn\'t in this room')
                    direction_command = input(
                        "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
            else:
                print('There are no items in this room')
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
    elif len(direction_command) == 1:
        if direction_command == "i":
            print("Inventory: ")
            for item in newPlayer.items:
                print(item.name, item.description)
            direction_command = input(
                "Press Enter to close inventory ").split(",")
        elif direction_command == "n":
            if room[newPlayer.current_room].n_to != None:
                newPlayer.current_room = room[newPlayer.current_room].n_to
                print(
                    f'{newPlayer.name} is now in the {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
                if len(room[newPlayer.current_room].items) != 0:
                    print(
                        f'There is a {room[newPlayer.current_room].items[0].name} here!')
                else:
                    pass
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
            else:
                print("There is no path in this direction")
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
        elif direction_command == "s":
            if room[newPlayer.current_room].s_to != None:
                newPlayer.current_room = room[newPlayer.current_room].s_to
                print(
                    f'{newPlayer.name} is now in the {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
                if len(room[newPlayer.current_room].items) != 0:
                    print(
                        f'There is a {room[newPlayer.current_room].items[0].name} here!')
                else:
                    pass
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
            else:
                print("There is no path in this direction")
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
        elif direction_command == "e":
            if room[newPlayer.current_room].e_to != None:
                newPlayer.current_room = room[newPlayer.current_room].e_to
                print(
                    f'{newPlayer.name} is now in the {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
                if len(room[newPlayer.current_room].items) != 0:
                    print(
                        f'There is a {room[newPlayer.current_room].items[0].name} here!')
                else:
                    pass
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
            else:
                print("There is no path in this direction")
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
        elif direction_command == "w":
            if room[newPlayer.current_room].w_to != None:
                newPlayer.current_room = room[newPlayer.current_room].w_to
                print(
                    f'{newPlayer.name} is now in the {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
                if len(room[newPlayer.current_room].items) != 0:
                    print(
                        f'There is a {room[newPlayer.current_room].items[0].name} here!')
                else:
                    pass
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
            else:
                print("There is no path in this direction")
                direction_command = input(
                    "What do you want to do now? (take,item_name), (drop,item_name) or press Enter to go enter other commands ").split(",")
        else:
            print(
                "Please enter n,s,e,w for directions, i for inventory or q to quit")
            direction_command = input(
                "Which way will you go? ")
print(f'Until next time, {newPlayer.name}!')
