number_to_be_guessed = 69
user_guess = int(input("Guess a number: "))
while user_guess < 3:

    if user_guess > number_to_be_guessed:
        print("Guess a lower number")
    elif user_guess < number_to_be_guessed:
        print("Guess a higher number")
    else:
        print("You guessed correctly")

    user_guess += 1
