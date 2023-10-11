'''
In this module there are all the actions the player might do during the game. 

'''

from day_cero_CharacterCreation import player_information
import random

inventory = {'wood': 0, 'minerals': {}, 'fish': []}
#Functions defining all the actions the character might do. They will be used later in the game according to different criteria

#Cleaning soil function

def clean_soil():
  """ This function allows the player to clean soil everytime is needed. 
      Might be useful for the beggining of the game and after season changes """
  print(f"{player_information['player_name']} Now you are facing a big land full of different problems. You'll go meter by meter to check all of the land and clean it properly \n")
  dirty_soil = ['weed', 'stick', 'stick', 'nothing', 'weed', 'root', 'weed', 'nothing', 'nothing','root', 'trash', 'nothing','weed']
  
  print('Lets begin cleaning! \n')
  for dirt in dirty_soil:
    if dirt == 'weed':
      print('One weed out!')
    elif dirt == 'stick':
      print('And one less stick')
    elif dirt == 'nothing':
      print('Finaaally some clean ground')
    elif dirt == 'root':
      print('One root down')
    else:
      print(f'Who leaved this here??? {dirt} ? Oh my god, the nerve!')

  energy_cost_clean_soil = 15
  player_information['energy'] = player_information['energy'] - energy_cost_clean_soil
  final_message = print(f"Finished! This action costed {energy_cost_clean_soil} energy points, so now you have {player_information['energy']} points left")

  return final_message
#Fishing function

def fishing():
  ''' This functions allows the player to fish.
   The fish captured will be stored in the player's inventory.
   It has less energy cost when the player has their farm near the river '''
  print(f'''Aw! It's so relaxing to fish in the river. You are sitting in some rocks surrounded by trees looking at a very wide river with transparent water.
  Take your fishing pole, {player_information['player_name']}!''')
  fishs = ['salmon', 'carp', 'trout', 'catfish', 'tilapia']
  global inventory
  random_fish = random.choice(fishs)
  print(f"Wow, you caught a {random_fish}!")
  
  inventory['fish'].append(random_fish)

  energy_cost_fishing = 10
  player_information['energy'] = player_information['energy'] - energy_cost_fishing
  final_message = print(f"Finished! This action costed {energy_cost_fishing} energy points, so now you have {player_information['energy']} points left")
  
  return final_message
#Mining function

def mining():
  ''' This function allows the mining of minerals. 
      The elements mined will be stored in the inventory of the player.
      This function costs less energy when the player lives near the mountain. '''
  print(f''' So, I've heard that you need some rocks and minerals, am I right {player_information['player_name']}? Let's mine then. Take your pike and begin excavating ''')
  rocks_minerals = ['rock', 'iron', 'rock', 'copper', 'copper', 'iron', 'diamond', 'rock', 'rock','rock','copper','rock']
  
  global inventory
  mineral_counts = inventory['minerals']
  
  if mineral_counts is None:
        mineral_counts = {}

  for mineral in rocks_minerals:
        mineral_counts[mineral] = mineral_counts.get(mineral, 0) + 1
  print('Nice job! You mined these minerals: ')
  for mineral, count in mineral_counts.items():
        print(f'{mineral}: {count}')
  print(f"That's very useful, {player_information['player_name']}")

  energy_cost_mining = 10
  player_information['energy'] = player_information['energy'] - energy_cost_mining
  #mineral_counts = inventory.get('minerals', {})
  inventory['minerals'] = mineral_counts
  final_message = print(f"Finished! This action costed {energy_cost_mining} energy points, so now you have {player_information['energy']} points left")
  
  return final_message

#Chopping trees function

def chopping_trees():
  ''' This function allows the player to chop down trees. 
      The wood chopped will be stored in the player's inventory.
      This actions has less energy cost when the player lives near the forest
      Each tree equals to 3 wood items '''
  print(f"Aha! I see! You need some wood, don't you {player_information['player_name']}? Take your axe, we'll go deep into the woods \n Just one thing. Each tree you chop, it's 5 energy points! Be careful")
  global inventory
  chopped_trees = 0
  total_trees = 10
  while chopped_trees < total_trees:
    
    print(f'Chopped down tree {chopped_trees}. Trees remaining: {total_trees - chopped_trees}')
    user_input = input('Want to keep chopping? Write Y to keep going and N to stop ')
    if user_input.upper() == 'N':
      break
    chopped_trees += 1 
  
  energy_cost_chop_trees = chopped_trees * 5
  total_wood = chopped_trees * 3
  inventory['wood'] += total_wood
  player_information['energy'] = player_information['energy'] - energy_cost_chop_trees
  final_message = print(f"Finished! Uf, what a workout. You chopped down {chopped_trees} trees. That costed {energy_cost_chop_trees} energy points, you have {player_information['energy']} points left")
  
  return final_message
