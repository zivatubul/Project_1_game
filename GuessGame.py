import random
def generate_number(difficulty):
    secret_number = random.randint(1,difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    guess_number = int(input(f'Please Guess an number between 1 to {difficulty}:'))
    return guess_number

def compare_results(guess_number , secret_number):
    if secret_number == guess_number:
        return True
    else:
        return False

def play(difficulty):
        secret_number = generate_number(difficulty)
        guess_number = get_guess_from_user(difficulty)
        return compare_results(guess_number, secret_number)





















