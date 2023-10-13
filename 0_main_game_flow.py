from day_cero_CharacterCreation import *
from day_one_FirstActivities import *
from day_two_InventoryPresentation import *
from day_three_MovingAround import *
from player_actions import * 
from general_actions import *

#Here's the general flow of the game

day_flow = {
    0: welcome_new_player,
    1: day_one,
    2: day_two,
    3: day_three
}
while True:

    current_day = end_of_day.counter

    if current_day in day_flow:
        day_flow[current_day]()
    else:
        day_count()
        print(f"Today we are on day {current_day}. So far, nothing special happens. Rest, brave traveler, hectic days are ahead")
        break
