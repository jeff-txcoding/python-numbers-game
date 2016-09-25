import random


def play_again():
    """ Run the game again if player doesn't enter 'n' """
    
    play = input("Do you want to play again? Y/n: ")
    if play != "n":
        game()
    else:
        print("Bye! Thanks for playing.")


def game():
    """ The main game function """

    secret_number = random.randint(1, 10)

    guess_list = []

    while len(guess_list) < 5:
        guess = input("Guess a number between 1 and 10: ")

        try:
            guess = int(guess)
        except ValueError:
            print("{} is not a number!".format(guess))
        else:
            if guess == secret_number:
                print("You guessed it! My number was {}".format(secret_number))
                play_again()
                break
            elif guess > secret_number:
                print("{} is too high!".format(guess))
            else:
                print("{} is too low!".format(guess))

            guess_list.append(guess)
    else:
        print("You ran out of guesses!")
        play_again()


game()
