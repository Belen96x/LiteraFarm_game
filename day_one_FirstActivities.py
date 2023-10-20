'''
In this module there is only the day one function. In this day the user is presented with both the clean soil activity and the
activity that is cheaper in energy cost according to the type of farm they have chosen. 
'''

from player_actions import *
from general_actions import *
from day_cero_CharacterCreation import *


def day_one():
  ''' This function has the main order for the first day on the farm.
      The first step would be cleaning the soil independently of the type of farm. This action is mandatory the first day.
      After that first step, the users have some particular options to work with according to the type of farm they have chosen.
      This actions have less energy cost. In this first day the player will be offered with just two opportunities to perform actions.
      If they refuse twice, the day will end.'''
  start_of_day()
  print(f''' 
          I hope you rested well yesterday because today? We have maaany things to do!
          First things first, {player_information['player_name']}. Look at the horrible state of this yard! 😐 So full of... everything...
          If we want to use it to grow food, uf. We'll need to do some work! Lets do it.
          This action costs 15 energy points. I know, it's a lot isn't it? But we have to do it to start! ''')
  
  kickstart = input(f"Are you ready, {player_information['player_name']}? Type anything to start!")
  
  if kickstart is not None:
     clean_soil()
  else:
     kickstart
  
  #Now that the first action is over, we will inform the player the options that they have so far
  
  print(f"Here we can do some actions according where we live! Some actions costs us less energy (because we are closer) \n I see you live near the {player_information['type_farm_choice']}. ")
  display_less_cost_energy_actions()

  if player_information['energy'] > 0:
    print(f"You are not so tired yet! Your energy levels are at {player_information['energy']} points!")
    
    display_less_cost_energy_actions()


    if action_choice.upper() == 'Y':
      print(f"That's it for today! Tomorrow, we'll do some more fun things {player_information['player_name']}!")
      
    elif action_choice.upper() == 'N':
      print(f"What a day, {player_information['player_name']}! I hope you rest well until tomorrow. We'll see more nice things to do. See you later 👋")       
  
    end_of_day()
    day_count()