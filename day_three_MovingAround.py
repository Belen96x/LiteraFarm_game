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
    
    distance_calculator_display(player_information, distances_forest)

    while player_information['type_farm_choice'] == player_information['current_location']:
        print(f"Hey!! I don't like tricks {player_information['player_name']}. You HAVE to move around. \n Don't choose {player_information['type_farm_choice']}, be curious")
        distance_calculator_display(player_information, distances_forest)
        break

    print(f''' Welcome, brave adventurer! Now you are in the {player_information['current_location']}!
               Here, we can do different things. But be cautious, you will have to come back home.
               For that, you will need energy. Do you understand? 
               Let's do some local actions here, and then go back home to {player_information['pet']['pet_name']} ''')
    
    display_less_cost_energy_actions()
    
    print(f'''Bravo, {player_information['player_name']}! Now you do something new and now how to do things further away from home
              Let's check your inventory to see what you gained in this little excursion ''')
    
    access_inventory(inventory)

    print(f"The night is coming. We must go back home asap, {player_information['player_name']}! Nights here are... dangerous ")

    back_home(player_information, distances_forest)

    if alert_away_from_home == True:
        print("Just for today, I'll let it pass. Here, take a sleeping bag. But hey, this will not last. ")
    else:
        print(f"Welcome home, explorer! {player_information['pet']['pet_name']} was driving me crazy already!! ")
    
    end_of_day()
    day_count()