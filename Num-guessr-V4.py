import random
import json
import datetime
current_time = datetime.datetime.now()

your_name = input("Please, enter your name: ")

sn = random.randint(1, 50)
attempt = 0
score_data = {"attempt": attempt, "date": datetime.datetime.now(), "secret": str(sn), "name": str(your_name)}

with open("score_list.txt", "r") as score:
    score_list = json.loads(score.read())
    print("Highscores: " + str(score_list[:3]))

for score_dict in score_list:
    print(your_name + " - " + str(score_dict["attempt"]) + " attempt, date: " + score_dict.get("date")
          + ", secret number: ")


while True:
    guess = int(input("Please, enter number between 1 and 50: "))
    attempt += 1
    wrong_guesses = [str(guess)]

    if guess == sn:
        score_list.append({"attempt": attempt, "date": str(datetime.datetime.now()), "name": your_name,
                           "secret": str(sn), "wrong": wrong_guesses})

        with open("score_list.txt", "w") as score:
            score.write(json.dumps(score_list))
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

wrong_guesses.append(guess)
