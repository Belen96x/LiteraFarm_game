#from general_actions import save_to_json
import json
'''
In this module there are three main functions:
1. The welcome_new_player, that allows us to create a new player in the game.
2. The day_count that allows us to follow the pass of the days
3. The end of the day function that closes the day
'''

player_information = dict()


def welcome_new_player():
  ''' This is the first function of the game. This function introduce the player to the game and allow us to get this relevant information
      1. Name
      2. Type of farm chosen
      3. Type of pet chosen
      4. Name of pet
      5. Name of the farm chosen
      All this information will be saved in the dictionary called <player_information>. The player will be informed as well that these initial values
      1. hp = 100
      2. energy = 100
      3. money = 0
      These are the default values set up by the system. All of them are also saved into the dictionary <player_information>
      This function must be executed just one time at the beginning of the game. '''
  
  #General information of the player. Obtain name and introduce them to the game.

  print('''Hello, traveler! Welcome to LiteraFarm 🏞
  You seem pretty tired. Don't worry! Here we can take make some room for you to relax. Let me present myself. I'm Lina, the guardian of this forest''')

  player_information['player_name'] = input("What's your name, brave traveler? ")

  print(f'''Oh, nice to meet you {player_information['player_name']}! I'm very happy to welcome you to my forest. It is very hard to find, so congratulations!
  Since you've been travelling for so long, I think you should get a little piece of my home to build your next life 👩‍🌾
  Lets make some choices to make you feel welcome''')

  #Choose the farm type

  type_farm = ['river', 'mountain','mid forest']

  player_information['type_farm_choice'] = ""

  while player_information['type_farm_choice'] not in type_farm:
    player_information['type_farm_choice'] = input(f'''
                         First, let me know where you prefer to live.
                         Would you like to be near the river, near the mountain or in mid forest?
                         Type {type_farm[0]} for living near the river ⛴
                         {type_farm[1]} for living near the mountain 🏔 and
                         {type_farm[2]} to live in the middle of the forest 🏕 ''')
    if player_information['type_farm_choice'] == type_farm[0]:
      print(f"Great choice {player_information['player_name']}! I think you should be very happy here. You will have more fish than in other parts of the forest. Enjoy it!")
    elif player_information['type_farm_choice'] == type_farm[1]:
      print(f"Nice choice {player_information['player_name']}! Here you will have more access to the mines, where you will find several useful resources")
    elif player_information['type_farm_choice'] == type_farm[2]:
      print(f"Wow, incredible choice {player_information['player_name']}! You will have access to so much wood here your house will be very big and nice")
    else:
      print(f"Hm, please, be careful and choose between {type_farm} choices, {player_information['player_name']}. Pay attention to your spelling!")

  print(f"Great progress, {player_information['player_name']}, now you have an amazing place to live! But remember, no life is worth living alone")

  #Choose pet type & name

  type_pet = ['cat', 'dog']

  player_information['pet'] = {'type_pet_choice': '', 'pet_name':''}

  while player_information['pet']['type_pet_choice'] not in type_pet: #Entering the next level of nested dictionaries
    player_information['pet']['type_pet_choice'] = input(f'''
                        Lets choose a pet to make you some company in this big forest! What do you prefer, {player_information['player_name']}?
                        Write either {type_pet[0]} or {type_pet[1]} ''')
    if player_information['pet']['type_pet_choice'] == type_pet[0]:
      print(f"Oh, great choice {player_information['player_name']}! I've got a cat myself. It's called Loki, maybe they can be friends in the future 🐱")
    elif player_information['pet']['type_pet_choice'] == type_pet[1]:
      print(f"Amazing, {player_information['player_name']}! I don't like so much dogs, but you know what? I'm glad you're happy and the little dog will be so happy along your side 🐕")
    else:
      print(f"Hm, please, be careful and choose between {type_pet} choices, {player_information['player_name']}. Pay attention to your spelling!")

  player_information['pet']['pet_name'] = input(f"Lets name the little one, {player_information['player_name']}! Choose a nice name for your pet ")

  print(f"{player_information['pet']['pet_name']}? Wow, sounds so nice!!")



  players_farm_name = input((f'''
                          You're almost set up for success {player_information['player_name']}.
                          But I almost forget something terribly important!!
                          Even though the forest is mine to keep, your little house must have a name to be recognised between all the inhabitants of this forest.
                          How would you name your beautiful new home? '''))

  #Set default values for general stats of the player

  player_information.setdefault('hp', 100)
  player_information.setdefault('energy', 100)
  player_information.setdefault('money', 0)
  player_information.setdefault('current_location', player_information['type_farm_choice'])

  final_data = print(f"Amazing, amazing choices {player_information['player_name']}. Let's review all of them. \n You will live in a farm close to the {player_information['type_farm_choice']} named {players_farm_name} \n You faitful companion will be a {player_information['pet']['type_pet_choice']} named {player_information['pet']['pet_name']}\n \n Seems so exciting! Just to let you know some stuff that is important.\n Here you will have some health status and energy. Now, your health is {player_information['hp']} and your energy is {player_information['energy']}\n Every time you do some actions those two things might get affected. So be careful! We want you energized and healthy.\n If those levels go down to cero, you will have to end the day and might even loose some money. I know, right now you don't have any money, don't you?\n I see your account says {player_information['money']}. Don't worry! Some actions will give you money. We'll get there!\n Enjoy your time here, brave traveler! I'll see you around 😉\n")
  
  end_of_day()
  day_count()

  save_to_json()

  return final_data

def end_of_day():
    ''' This function will execute at the end of each day'''
    print(f"This was a good day {player_information['player_name']}. Today you have {player_information['energy']} energy points left, \n you have {player_information['hp']} health points \n and you have {player_information['money']} money left. See you tomorrow!\n ")

end_of_day.counter = 0

def day_count():
     '''
     This functions tracks the pass of days
     '''
     end_of_day.counter +=1 
     return end_of_day.counter

def save_to_json():
    with open('player_information.json', 'w') as json_file:
        json.dump(player_information, json_file)
    print("Player information saved to player_information.json.")
