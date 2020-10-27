secret = 42
guess = -3

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 50): "))

    if guess == secret:
        print("You guessed it - congratulations! It's number " + str(secret))
    else:
        print("Sorry, your guess is not correct... The secret number is not " + str(guess) + ".")
