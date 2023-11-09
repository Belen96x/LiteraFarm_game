'''
This class will allow to create multiple players with their default settings. It's an improvement from the 
previous method that worked only with dictionaries. The properties that the player will have, so far, are:

    1. Player name
    2. Type farm chosen
    3. Farm name
    4. Pet type
    5. Pet name

Some default values are setted as well:
    1. Current location, that will equal to type farm chosen at the very begining
    2. Hp = 100
    3. Energy = 100
    4. Money = 0

This class will be updated with methods that the player can execute further on. So far, it's not implemented in the code. 
It will be implemented later on. But this is a start. 
'''

class player:
    def __init__(self, player_name = None, type_farm_choice = None, farm_name = None, type_pet = None, pet_name = None, hp=100, energy=100, money=0):
        self.player_name = player_name
        self.type_farm_choice = type_farm_choice
        self.current_location = type_farm_choice
        self.farm_name = farm_name
        self.type_pet = type_pet
        self.pet_name = pet_name
        self.hp = hp
        self.energy = energy
        self.money = money
    
    def setPlayerName(self):
      name = str(input("What's your name, brave traveler? "))
      self.player_name = name

    def getPlayerName(self):
      return self.player_name
    
    def setPlayerTypeFarm(self):
        
        type_farm = ['river', 'mountain','mid forest']

        choice = None

        while choice not in type_farm:
          choice = input(f'''
                              First, let me know where you prefer to live.
                              Would you like to be near the river, near the mountain or in mid forest?
                              Type {type_farm[0]} for living near the river ⛴
                              {type_farm[1]} for living near the mountain 🏔 and
                              {type_farm[2]} to live in the middle of the forest 🏕 ''')
          if choice == type_farm[0]:
            print(f"Great choice {self.getPlayerName()}! I think you should be very happy here. You will have more fish than in other parts of the forest. Enjoy it!")
          elif choice == type_farm[1]:
            print(f"Nice choice {self.getPlayerName()}! Here you will have more access to the mines, where you will find several useful resources")
          elif choice == type_farm[2]:
            print(f"Wow, incredible choice {self.getPlayerName()}! You will have access to so much wood here your house will be very big and nice")
          else:
            print(f"Hm, please, be careful and choose between {type_farm} choices, {self.getPlayerName()}. Pay attention to your spelling!")
        
        self.type_farm_choice = choice
        self.current_location = choice
      
    def getPlayerTypeFarm(self):
      return self.type_farm_choice
    
    def setFarmName(self):
      players_farm_name = input((f'''
                          You're almost set up for success {self.getPlayerName()}.
                          But I almost forget something terribly important!!
                          Even though the forest is mine to keep, your little house must have a name to be recognised between all the inhabitants of this forest.
                          How would you name your beautiful new home? '''))
      self.farm_name = players_farm_name
    def getFarmName(self):
      return self.farm_name
    
    def setPetType(self):
      type_pet = ['cat', 'dog']
      pet_type = None
      while pet_type not in type_pet: #Entering the next level of nested dictionaries
          pet_type = input(f'''
                            Lets choose a pet to make you some company in this big forest! What do you prefer, {self.player_name}?
                            Write either {type_pet[0]} or {type_pet[1]} ''')
          if pet_type == type_pet[0]:
            print(f"Oh, great choice {self.player_name}! I've got a cat myself. It's called Loki, maybe they can be friends in the future 🐱")
          elif pet_type == type_pet[1]:
            print(f"Amazing, {self.player_name}! I don't like so much dogs, but you know what? I'm glad you're happy and the little dog will be so happy along your side 🐕")
          else:
            print(f"Hm, please, be careful and choose between {type_pet} choices, {self.player_name}. Pay attention to your spelling!")
      self.type_pet = pet_type
    def getPetType(self):
      return self.type_pet

    def setPetName(self):
      pet_name = input(f"Lets name the little one, {self.player_name}! Choose a nice name for your pet ")
      self.pet_name = pet_name

    def getPetName(self):
      return self.pet_name
    
    def getEnergy(self):
      return self.energy
    def getMoney(self):
      return self.money
    def getHp(self):
      return self.hp