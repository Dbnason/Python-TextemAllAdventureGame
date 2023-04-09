# Text based Adventure Game
# IT 140
# Created by Darren Nason

#
# Dict for all rooms the user will move through
#

rooms = {'You see a fork in the road': {'south': 'You go through the grown up forest', 'east':
    'You went to an old farmhouse'},
         'You go through the grown up forest':
             {'south': 'Arrived at the castle of wizardry', 'west': 'Ancient Armory',
              'north': 'You see a fork in the road',
              'east': 'The bonfire grows cold the boss is near', 'item': 'map'},
         'You went to an old farmhouse': {'west': 'You see a Fork in the road'},
         'Arrived at the castle of wizardry': {'west': 'Found an old knights dungeon', 'east':
             'You are standing in front of a three-headed monster aka a cerberus',
                                               'north': 'You go through the grown up forest',
                                               'item': 'ability to cast magic'},
         'Ancient Armory': {'east': 'You go through the grown up forest', 'item': 'Sharpened Sword'},
         'Found an old knights dungeon': {'east': 'Arrived at the castle of wizardry', 'item': 'Old knights armor set'},
         'The bonfire grows cold the boss is near': {'north': 'The evil minotaur boss',
                                                     'west': 'You go through the grown up forest',
                                                     'item': 'Bonfire kindling'},
         'You are standing in front of a three-headed monster aka a cerberus':
             {'west': 'Arrived at the castle of wizardry', 'item': 'slay the cerberus and enhanced blade skill'},
         'The evil minotaur boss':
             {'south': 'The bonfire grows cold the boss is near'}
         }

#
# Set Starting room and read in exits user can choose and ask the user if ready to play and empty list to collect items
#
user_inventory = []
current_room = 'You see a fork in the road'
exits = rooms[current_room]
user_move = input('Do you want to play or quit? \n')
rooms.get('item')


def main():
    global user_move

    #
    # Set up instructions for the game
    #

    def game_instructions():
        print('--------------Instructions---------------')
        print('Directions are North/South/East/West')
        print('In order to pick up the item answer the prompt')
        print('In order to win the game you have to successfully find the 6 items in the rooms and pick them up')
        print('Without running into the evil boss Good luck!\n')

    #
    # define function to check and move through rooms
    #
    def move_to_locations():
        global current_room
        global exits
        exits = rooms[current_room]
        if user_move in rooms[current_room]:
            current_room = exits[user_move]
            exits = rooms[current_room]
        else:
            print('cannot go that way! Choose a different direction! \n')

    #
    # function to look and pick up items
    #
    def get_item():
        global item
        if item in user_inventory or item is None:
            pass
        global pickup
        if item is not None and pickup == 'yes':
            if item in user_inventory:
                print('You already have this item in your inventory!')
            else:
                user_inventory.append(item)
                print('You have acquired', item, '\n')

    #
    # function for user to see inventory
    #
    def player_status():
        print('current room is', current_room, '\n')
        print('Possible directions are',list(exits.keys()))
        global pickup
        global item
        global user_inventory
        item = rooms[current_room].get('item')
        print('You are carrying', user_inventory, '\n')
        if item not in user_inventory and not None:
            print('You found a', item)
            pickup = input('Do you want to pick up the item? ')

    #
    # loop for the user to play until keyword quit
    #
    game_instructions()
    print(current_room)
    while user_move != 'quit':
        user_move = input('Enter a Direction North/South/East/West: ').lower()
        move_to_locations()
        player_status()
        get_item()
        if len(user_inventory) == 6:
            print('You have won the Game congrats on slaying the evil beast!')
            break
        elif current_room == 'The evil minotaur boss':
            print('You lost the game, but you can always play again!')
            break
    print('Hope you enjoyed the game!')


main()
