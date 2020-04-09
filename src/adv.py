from room import Room
from player import Player

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

# Make a new player object that is currently in the 'outside' room.

newPlayer = Player("Jeff Goldblum", "outside")


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


update = print(
    f'{newPlayer.name}\'s current position: {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')


direction_command = input("Which way will you go? (n,s,e,w) Press q to quit ")

while not direction_command == "q":
    if direction_command == "n":
        if room[newPlayer.current_room].n_to != None:
            newPlayer.current_room = room[newPlayer.current_room].n_to
            print(
                f'{newPlayer.name}\'s current position: {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
            direction_command = input(
                "Which way will you go? ")
        else:
            print("There is no path in this direction")
            direction_command = input(
                "Which way will you go? ")
    elif direction_command == "s":
        if room[newPlayer.current_room].s_to != None:
            newPlayer.current_room = room[newPlayer.current_room].s_to
            print(
                f'{newPlayer.name}\'s current position: {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
            direction_command = input(
                "Which way will you go? ")
        else:
            print("There is no path in this direction")
            direction_command = input(
                "Which way will you go? ")
    elif direction_command == "e":
        if room[newPlayer.current_room].e_to != None:
            newPlayer.current_room = room[newPlayer.current_room].e_to
            print(
                f'{newPlayer.name}\'s current position: {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
            direction_command = input(
                "Which way will you go? ")
        else:
            print("There is no path in this direction")
            direction_command = input(
                "Which way will you go? ")
    elif direction_command == "w":
        if room[newPlayer.current_room].w_to != None:
            newPlayer.current_room = room[newPlayer.current_room].w_to
            print(
                f'{newPlayer.name}\'s current position: {room[newPlayer.current_room].name}. {room[newPlayer.current_room].description}')
            direction_command = input(
                "Which way will you go? ")
        else:
            print("There is no path in this direction")
            direction_command = input(
                "Which way will you go? ")
    else:
        print("Please enter n,s,e,w or q to quit")
        direction_command = input(
            "Which way will you go? ")
print("Thanks for playing! Goodbye.")
