'''
In this module there will be functions that could be transversal to any day. These are not callable by the user in any point.
Here you might find general functions to control the time of the day, inventory control among others.
'''

from day_cero_CharacterCreation import *
from player_actions import *

#Inventory creation for the player



#Options for less energy cost for the player. Display them.

def less_cost_energy_actions():
    ''' This options will be offered any time the player has the chance to chose this actions with less energy cost. '''
    if player_information['type_farm_choice'] == 'river':
          fishing()    
    elif player_information['type_farm_choice'] == 'mid forest':
          chopping_trees() 
    elif player_information['type_farm_choice'] == 'mountain':
          mining()

#This function will be performed at the beginning of each day

def start_of_day():
     '''This function will execute at the beginning of each day. It selects randomly the weather for the day.
        Each start of the day means that the hp and the health go backs to 100'''
     player_information['hp'] = 100  
     player_information['energy'] = 100
     weather = ['sunny', 'rainy', 'windy'] 
     print(f"Good morning, {player_information['player_name']}! Nice to see you")
     weather_today = random.choice(weather)
     print(f'''Today the day seems to be {weather_today}. Pay attention to that to plan ahead your day!
               Right now we are in day {end_of_day.counter} ''')
     season()
     print(f"Today we are in {season_right_now}. Your health is back to {player_information['hp']} and your energy is also on {player_information['energy']}")
     start = input('Ready to start? Press enter!')
     start

#Season tracker

season_right_now = ''

def season():
    '''
    This function will control the pass of the seasons. Each season passes when 5 days pass.
    '''
    global season_right_now
    seasons = ['spring', 'autumn', 'winter', 'summer']

    if end_of_day.counter <= 5:
        season_right_now = seasons[0]
    elif end_of_day.counter == 10:
        season_right_now = seasons[1]
    elif end_of_day.counter == 15:
        season_right_now = seasons[2]
    else:
        season_right_now = seasons[3]

    return season_right_now

def access_inventory():
     '''
     This function allows the player to check the inventory
     '''
     print(f"These are all the things you have so far {inventory}\n")

action_choice = ''

def display_less_cost_energy_actions():

      '''
      This function displays the actions that costs less energy

      '''
      if player_information['type_farm_choice'] == 'river':
            print(f"You can do some {fishing.__name__}. This action costs 10 energy points")
      elif player_information['type_farm_choice'] == 'mid forest':
            print(f"You can do some {chopping_trees.__name__}. This action costs 10 energy points")
      else:
            print(f"You can do some {mining.__name__}. This action costs 10 energy points")
      
      global action_choice
      action_choice = input(f"Would you like to do that right now {player_information['player_name']}? Type Y to do it and N to not do anything ")

      if action_choice.upper() == 'Y':
            less_cost_energy_actions()
      else:
            print('I see you are a little bit tired, I see!')

