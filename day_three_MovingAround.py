from player_actions import *
from general_actions import *
from day_cero_CharacterCreation import *

'''
In this module it will be only the day three activites of the game

'''

def day_three():
    '''
    In this day the user will be presented with the options of moving around the forest and do actions further away from the farm.
    This action will have an added energy cost due to the energy cost of moving further away.

    '''
    start_of_day()

    print('You seem a little bit bored ' + player_information['player_name'] + ' '+ 'Want to move around and know more about the forest?')

    kickstart = input(f"Are you ready, {player_information['player_name']}? Type anything to start!")
  
    if kickstart is not None:
        print(f'''Ok! See, here you can do more things than just the ones that are closer to you. 
                  But, in order to do that, we'll need to walk a bit. So far, you can only walk.
                  Later on you might find a way to move faster. Let's try moving a bit''')
    else:
        kickstart
    
    display_distances()

    end_of_day()
    day_count()