import random


def play_game():
    print("🎮 Welcome to the Number Guessing Game!")
    name = input("Enter your name: ")

    secret_number = random.randint(1, 200)
    max_attempts = 6

    print(f"\nHello {name}!")
    print("I am thinking of a number between 1 and 200.")
    print(f"You have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess < 1 or guess > 200:
                print("❌ Please enter a number between 1 and 200.\n")
                continue

            if guess < secret_number:
                print("📉 Too low!\n")
            elif guess > secret_number:
                print("📈 Too high!\n")
            else:
                print(f"🎉 Congratulations {name}! You guessed the number in {attempt} attempts.")
                return

        except ValueError:
            print("❌ Please enter a valid number.\n")

    print(f"\n😔 Game Over! The correct number was {secret_number}.")


while True:
    play_game()

    choice = input("\nDo you want to play again? (yes/no): ").strip().lower()

    if choice not in ["yes", "y"]:
        print("👋 Thanks for playing!")
        break
