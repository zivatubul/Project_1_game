import random
import time
from Utils import screen_cleaner
def generate_sequence(difficulty):
    random_list = [0] * difficulty
    for i in range(len(random_list)):
        number = random.randint(1, 101)
        random_list[i] = number
    print(random_list)
    time.sleep(0.7)
    screen_cleaner()
    return random_list

def get_list_from_user(difficulty):
    print ("After seeing the numbers enter the numbers you saw, each one separated with Enter")
    user_list = [0] * difficulty

      # iterating till the range
    for i in range(difficulty):
        user_input = int(input("Please choose a number:"))
        user_list[i] = user_input  # adding the element
    return user_list

def is_list_equal(computer_list, user_list):
    if computer_list == user_list:
        return True
    else:
        return False

def play1(difficulty): # calling the function abov
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    return is_list_equal(list_a,list_b)