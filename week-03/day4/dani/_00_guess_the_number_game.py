from random import randint

def get_integer():
    number = int(input("Your guess: "))
    return number

num_to_guess = randint(0,10)
chances = 5
number_of_guesses = chances

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("You entered a wrong value")
    else:
        if guess < num_to_guess:
            print(' Bigger than ' + str(guess) )
        elif guess > num_to_guess:
            print(' Smaller than ' + str(guess))
        else:
            print(" You are goddam' right!")
            break

        number_of_guesses -= 1
        if number_of_guesses == 0:
            print("You had %d chances to guess %d, looser" %(chances, num_to_guess))
            break
