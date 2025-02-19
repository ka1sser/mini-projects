# Topic: Random module
# Rock, Paper, Scissors game
import random

options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        print()
        player = input("Enter a choice (rock, paper, or scissors): ")

    print(f"\nPlayer: {player}")
    print(f"Computer: {computer}\n")

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win!\n")
    elif player == "scissors" and computer == "paper":
        print("You win!\n")
    elif player == "paper" and computer == "rock":
        print("You win!\n")
    else:
        print("You lose!\n")

    play_again = input("Play again? (y/n): ").lower()

    if not play_again == "y":
        running = False

print("\nThanks for playing!")
