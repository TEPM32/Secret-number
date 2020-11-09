import datetime
import json
import random

player = input("Please, enter your name: ")

secret = random.randint(1, 50)
attempts = 0

with open("Scoresheet.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

# print(sorted(score_list.attempts()))
# sorted_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]
sorted_score_list = sorted(score_list.attempts, reverse=True, key=lambda x: x[1])

for element in sorted_score_list:
    print(element[:3])

for score_dict in score_list:
    score_text = "{0} - {1} attempts, date: {2}. Secret number: {3}. Wrong guesses: {4}".format(score_dict.get("player_name"),
                    score_dict.get("attempts"), score_dict.get("date"), score_dict.get("secret_number"),
                    score_dict.get("wrong_guess"))
    print(score_text)

wrong_guess = []

while True:
    guess = int(input("Guess the secret number (between 1 and 50): "))
    attempts += 1

    if guess == secret:
        score_list.append({"attempts": attempts, "date": str(datetime.datetime.now()), "player_name": player,
                           "secret_number": secret, "wrong_guess": wrong_guess})

        with open("Scoresheet.txt", "w") as score_file:
            score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))
        break
    elif guess > secret:
        if guess > 51:
            print("Try with number inside the given range.")
        else:
            print("Try with smaller number.")
    elif guess < secret:
        if guess < 1:
            print("Try with number inside the given range.")
        else:
            print("Try with bigger number.")

wrong_guess.append("\n" + str(guess))
