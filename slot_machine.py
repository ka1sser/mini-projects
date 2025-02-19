# Topic: Functions
# Slot Machine program
import random
import time


def spin_row():
    symbols = ["🍒", "🍉", "🍋", "🔔", "⭐"]

    return [random.choice(symbols) for symbol in range(3)]


def print_row(row):
    print("************************")
    print(" | ".join(row))
    print("************************\n")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🍋":
            return bet * 5
        elif row[0] == "🔔":
            return bet * 10
        elif row[0] == "⭐":
            return bet * 20
    return 0


def main():
    balance = 100

    print("************************")
    print("Welcome to Python Slots ")
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print("************************")

    while balance > 0:
        print(f"\nCurent balance: ${balance}")

        bet = input("Place your bet amount: ")

        if not bet.isdigit():
            print("Please enter a valid number, ya fool!")
            continue

        bet = int(bet)

        if bet > balance:
            print("Insufficient funds, ya fool!")
            continue

        if bet <= 0:
            print("Bet must be greater than 0.")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning...\n")
        time.sleep(1)
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}!")
        else:
            print("Sorry you lost this round.")

        balance += payout

        play_again = input("Spin again? (Y/N): ").upper()

        if play_again != "Y":
            break

    print("\n********************************************")
    print(f"Game over! Your final balance is ${balance}")
    print("********************************************")


if __name__ == "__main__":
    main()
