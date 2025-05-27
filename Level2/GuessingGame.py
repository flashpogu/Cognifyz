"""Write a Python program that generates a
random number between 1 and 100. The
user should then try to guess the number.
The program should provide hints such as
"too high" or "too low" until the correct
number is guessed."""

import random
def guessing_game():
    target_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I have selected a number between 1 and 100.")
    
    while True:
        guess = int(input("Please enter your guess: "))
        attempts += 1
        
        if guess < 1 or guess > 100:
            print("Your guess is out of bounds. Please guess a number between 1 and 100.")
            continue
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {target_number} in {attempts} attempts.")
            break
        
print(guessing_game())