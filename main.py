# Guess the number
# importing random
import random
# choosing a random number from 1 to 100
def choosing_number():
    return random.randint(1, 100)


# choosing the difficulty
def difficulty():
    difficult_level = input("Choose the difficulty. Type 'easy' or 'hard'. ")
    if difficult_level == 'hard':
        return 5
    else:
        return 10


# making a guess
def guessing(picked_number, attempts):
    guess = 0
    while guess != picked_number:
        print(f'You have {attempts} attempts remaining to guess the number. ')
        guess = int(input("Make a guess: "))
        attempts -= 1
        if guess > picked_number:
            print("Too high, Guess again. ")
        elif guess < picked_number:
            print("Too low, Guess again. ")
        if attempts == 0:
            return f"You've run out of guesses, you lost. \nThe number was {picked_number}"

    return f"You got it right it was {guess}. "


def guess_the_number():
    from art import logo
    print(logo)
    print("I'm thinking of a number between 1 and 100. ")
    chosen_number = choosing_number()

    attempts = difficulty()
    print(guessing(chosen_number, attempts))


print("Welcome to the Guess The Number game. ")
play = input("would you like to play? 'y' or 'n': ")
if play == 'y':
    guess_the_number()
else:
    print("Goodbye :).")
