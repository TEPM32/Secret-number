import random

sn = random.randint(1, 50)
attempt = 0

score = open("Scoresheet.txt", "r")
highscore = int(score.read())
print("Highscore: " + str(highscore))

while True:
    guess = int(input("Please, enter number between 1 and 50: "))
    attempt += 1

    if guess == sn:
        if attempt < highscore:
            open("Scoresheet.txt", "w")
            score.write(str(attempt))
            print("Congratulations! You have guessed it correctly. It is number " + str(sn))
            print("\n" + "End of the game.")
            break
    elif guess < sn:
        if guess < 1:
            print("Try with number inside the given range.")
        else:
            print("Try with bigger number.")
    elif guess > sn:
        if guess > 51:
            print("Try with number inside the given range.")
        else:
            print("Try with smaller number.")
