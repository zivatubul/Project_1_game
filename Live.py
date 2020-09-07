from Utils import ERROR_MESSAGE
from MemoryGame import play1
from GuessGame import play
from Score import add_score

def welcome():
    name = input('Please Enter your name: ')
    print('Hello  ' + name   + "  and welcome to the World of Games (WoG).Here you can find many cool games to play")

def check_inputs(user_input,difficulty):
    if user_input != 1 and user_input !=2:
        print(ERROR_MESSAGE)
    if difficulty not in [1,2,3,4,5]:
        print(ERROR_MESSAGE)
    if user_input == 1:
        result = play1(difficulty)
        if result == True:
            add_score(difficulty)
    if user_input == 2:
        result = play(difficulty)
        if result == True:
            add_score(difficulty)



def load_game():
    print('Please choose a game to play:')
    print('     1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back')
    print("     2. Guess Game - guess a number and see if you chose like the computer")
    user_input = int(input('Please enter your choice 1/2:' ))
    difficulty = int(input ('Please choose game difficulty from 1 to 5: '))
    check_inputs(user_input, difficulty)



