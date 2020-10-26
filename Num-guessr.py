secret = 42

guess = int(input("Guess the secret number between 1 and 50: "))

if guess == secret:
    print("Weldone! You have guessed it correctly.")
    print("End of the game")
elif guess > 50 or guess < 0:
    print("Try with the number within the given range.")
else:
    print("Your guess is incorrect.")
