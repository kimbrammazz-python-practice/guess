import random

def guess(x):
    random_number = random.randint(1, x)   
    # print(guess_number)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f'Guess a number between 1 and {x}: '))
        if guess_number < random_number:
            print('Too low, guess again')
        elif guess_number > random_number:
            print('Too high, guess again')
      
    print(f'Correct, you have guessed the correct number {random_number}!')        

guess(10)