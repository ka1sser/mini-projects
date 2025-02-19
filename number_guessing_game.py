# Topic: Random module
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)

guesses = 0
is_running = True

print()
print("--- Python Number Guessing Game ---\n")
print(f"Select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("That number is out of range, ya fool!\n")
        elif guess < answer:
            print("Too low! Try again!\n")
        elif guess > answer:
            print("Too high! Try again!\n")
        else:
            print(f"\nCORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}\n")
            is_running = False

    else:
        print("\nInvalid guess, ya fool!")
        print(f"Please select a number between {lowest_num} and {highest_num}\n")
