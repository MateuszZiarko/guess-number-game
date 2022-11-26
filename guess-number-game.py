import random


def play():
    print("You can guess the number or computer can guess the number")
    decision = input("Do you want to guess the number? Yes or No: ").lower()
    if decision == "yes":
        x = int(input("Choose maximum number, start number is 1: "))
        guess(x)
    if decision == "no":
        decision2 = input("Do you want computer to guess the number? Yes or No, writing No will end the game: ").lower()
        if decision2 == "yes":
            x = int(input("Choose maximum number, start number is 1: "))
            print(f"Computer will choose number between 1 and {x}")
            computer_guess(x)
        else:
            print("game over")
            quit()


def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again, too low.")
        elif guess > random_number:
            print("Sorry, guess again, too high")
    print(f"You have guessed the number {random_number} correctly!")
    play_again = input("Do you want to play again? Yes or No: ").lower()
    if play_again != "yes":
        print("game over")
        quit()
    else:
        play()

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # could also me high because low = high
        feedback = input(f"is {guess} to high (H), too low (L), or correct (C)?: ").lower()
        if feedback == "h":
            high = guess -1
        if feedback == "l":
            low = guess +1
    print(f"The computer guessed your number, {guess}, correctly!")
    play_again = input("Do you want to play again? Yes or No: ").lower()
    if play_again != "yes":
        print("game over")
        quit()
    else:
        play()



play()