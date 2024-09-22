import random, sys

user_guess = 0
guess_count = 0
print("This is a guess the number game.")
while True:
    secret_number = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20.")
    print("You have 6 chances to guess it.")
    for i in range(6):
        user_guess = int(input("Your guess: "))
        if user_guess < secret_number:
            print("That's too low.")
            guess_count = guess_count + 1
        elif user_guess > secret_number:
            print("That's too high.")
            guess_count = guess_count + 1
        else:
            guess_count = guess_count + 1
            break
    if user_guess == secret_number:
        print("Hey! Nice! You guessed it in " + str(guess_count) + " guesses!")
    else:
        print("Aww, you're out of guesses. The number was " + str(secret_number) + ". Better luck next time.")
    again = input("Play again? Y/N ")
    if again == "N" or again == "n" or again == "No" or again == "no":
        sys.exit()
    guess_count = 0
    print("")
