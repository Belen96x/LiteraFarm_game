'''
In this module there are all the actions the player might do during the game. 

'''

from day_cero_CharacterCreation import player_information
import random

inventory = {'wood': 0, 'minerals': {}, 'fish': []}

distances_forest = {'community_center': 0, 'river': 5, 'mid forest': 10, 'mountain': 15}

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
        This action has less energy cost when the player lives near the forest
        Each tree equals 3 wood items '''
    print(f"Aha! I see! You need some wood, don't you {player_information['player_name']}? Take your axe, we'll go deep into the woods \n Just one thing. Each tree you chop, it's 5 energy points! Be careful")
    global inventory
    total_trees = 10

    def chop_tree(chopped_trees=0):
        nonlocal total_trees

        if chopped_trees >= total_trees or player_information['energy'] <= 0:
            final_message = print(f"Finished! Uf, what a workout. You chopped down {chopped_trees} trees. You have {player_information['energy']} energy points left")
            return final_message

        print(f'Chopped down tree {chopped_trees}. Trees remaining: {total_trees - chopped_trees}')
        user_input = input('Want to keep chopping? Write Y to keep going and N to stop ')

        if user_input.upper() == 'Y':
            player_information['energy'] -= 5  # Deduct energy for each tree chopped
            inventory['wood'] += 3  # Add wood to inventory for each tree chopped
            return chop_tree(chopped_trees + 1)
        else:
            final_message = print(f"Finished! Uf, what a workout. You chopped down {chopped_trees} trees. You have {player_information['energy']} energy points left")
            return final_message

    return chop_tree()

def distance_calculator_display(player_information, distances_forest):
    '''
    This will calculate the distance from a place to another and display it to the user along with the energy cost for that walking 
    If the user agrees with this, he will be there and the actions of that location will be available to them.
    '''
    while True:
        location_2 = input('Where do you want to go?\nType "river", "mountain", or "mid forest" ')
        if location_2 in distances_forest:
            break 
        else:
            print("Psst!! Check your spelling")

    current_location = player_information.get('current_location')

    if current_location in distances_forest and location_2 in distances_forest:
        current_distance = distances_forest[current_location]
        location_2_distance = distances_forest[location_2]

        distance = abs(current_distance - location_2_distance)

        energy_cost_distance = distance * 3

        print(f'To get to {location_2} you have to walk {distance} kilometers. That costs {energy_cost_distance} energy points')
        mooving_choice = input('Do you want to go? Type Y to do it and N to stay here ')

        if mooving_choice.upper() == 'Y':
          player_information['energy'] = player_information['energy'] - energy_cost_distance
          player_information['current_location'] = location_2
        else:
          print(f"Ok! We'll stay in {current_location} a little bit more ")

        return distance, energy_cost_distance

alert_away_from_home = None

def back_home(player_information, distances_forest):
    '''
    This function allows the player to go back home after moving to another location
    '''
    global alert_away_from_home

    home_location = player_information.get('type_farm_choice')
    current_location = player_information.get('current_location')

    if home_location != current_location and home_location in distances_forest and current_location in distances_forest:
        home_distance = distances_forest[home_location]
        current_distance = distances_forest[current_location]

        distance_to_home = abs(home_distance - current_distance)
        energy_cost_distance = distance_to_home * 3

        print(f"To get back home to your home in the {home_location} from {current_location}, you have to walk {distance_to_home} kilometers. That costs {energy_cost_distance} energy points.")
        move_choice = input('Do you want to go back home? Type Y to do it and N to stay here ')


        if move_choice.upper() == 'Y':
          alert_away_from_home = False
          player_information['energy'] = player_information['energy'] - energy_cost_distance
          player_information['current_location'] = home_location
        elif move_choice.upper() == 'N':
          alert_away_from_home = True
          print(f"You decide to stay in {current_location} ")
        else:
          print(f"Hm. I think I don't understand you! {move_choice}")
    if alert_away_from_home == True:
      print("Just for today, I'll let it pass. Here, take a sleeping bag. But hey, this will not last. ")
    else:
      print(f"Welcome home, explorer! {player_information['pet']['pet_name']} was driving me crazy already!! ")

    return alert_away_from_home