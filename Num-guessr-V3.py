import random

sn = random.randint(1, 50)
attempts = 0
guess = -3

for a in range(5):
    guess = int(input("Guess the secret number between 1 and 50: "))

    if sn == guess:
        print("Welldone! You have guessed it correctly. It was number " + str(guess) + ".")
        break
    elif sn < guess:
        if guess > 50:
            print("Try with the number between 1 and 50.")
        else:
            print("Your guess is incorrect. Try with smaller number.")
    elif sn > guess:
        if guess < 1:
            print("Try with the number between 1 and 50")
        else:
            print("Your guess is incorrect. Try with bigger number.")

print("End of the game")
