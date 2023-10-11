from general_actions import *
from player_actions import *
from day_cero_CharacterCreation import player_information

'''
In this module there is only the day two function. 

'''

def day_two():
    '''
    In this second day the user will be presentated with the inventory and how to access it.
    Will be presented as well with the chance to perform actions further away from their farm.
    The store will be presented as well.
    
    '''
    start_of_day()

    print(f'''Hey, {player_information['player_name']}! I almost fall to the ground because of these things laying around
              That's NOT cool. Here, take this, use this vault to keep everything safe.
              I took the time to put your things there. But honestly? If I didn't like you as I do, I'd throw them all to the river.
              Let's start over\n''')
    
    access_inventory()

    print(f'''Okay, so now you see how your vault is organized. 
              We'll gather some materials now, with the proper order you know? To grow the vault bigger!
              I see you live near the {player_information['type_farm_choice']} \n''')
    
    display_less_cost_energy_actions()

    print(f"Well, let's see how you inventory grows!")

    access_inventory()

    print(f'''Amazing, {player_information['player_name']}! Now you now where to store properly your things.
              The whole forest thanks you for that.
              Let's try something. Try to access it by yourself''')
    
    access_vault = input("Type <inventory> to access your vault ")

    while access_vault != 'inventory':
        print('Ups, wrong spelling. Check again!')
        access_vault = input("Type <inventory> to access your vault ")
    access_inventory()
    
    print(f"Look at you go!! Nice, you are learning how to move around here, aren't you? Organizing it's so exhausting. I need a nap now \n")

    end_of_day()
    day_count()

