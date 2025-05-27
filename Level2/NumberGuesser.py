"""Create a number guessing game where the
program generates a random number
between a specified range, and the user tries
to guess it. Provide feedback to the user if
their guess is too high or too low."""

import random
def number_guesser():
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    if lower_bound >= upper_bound:
        print("Invalid range. Lower bound must be less than upper bound.")
        return
    
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0
    
    while True:
        guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
        attempts += 1
        
        if guess < lower_bound or guess > upper_bound:
            print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
            continue
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break

print(number_guesser())