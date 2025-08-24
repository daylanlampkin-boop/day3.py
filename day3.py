num = int(input("Enter a number: "))
if num % 4 == 0:
    print("That number is divisible by 4.")
elif num % 2== 0:
    print("That number is even.")
else:
    print("That number is odd.")
import random

def play(lo=1, hi=100):
    secret = random.randint(lo, hi)
    attempts = 0
    print(f"\nI'm thinking of a number between {lo} and {hi}.")

    while True:
        raw = input("Your guess (or 'q' to quit): ").strip()
        if raw.lower() == 'q':
            print(f"Bye! The number was {secret}.")
            return

        if not raw.isdigit():
            print("Please enter a whole number.")
            continue

        guess = int(raw)
        if not (lo <= guess <= hi):
            print(f"Stay in range {lo}–{hi}.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print(f"Correct! You got it in {attempts} tries.")
            return

def choose_level():
    level = input("Difficulty (easy/normal/hard): ").strip().lower()
    if level == "easy":
        return 1, 50
    elif level == "hard":
        return 1, 500
    return 1, 100

def main():
    while True:
        lo, hi = choose_level()
        play(lo, hi)
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
