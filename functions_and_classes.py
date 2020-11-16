import datetime
import json
import random

class game_res:
    def __init__(self, attempts, player_name, date):
        self.attempts = attempts
        self.player_name = player_name
        self.date = date

def play():
    secret = random.randint(1, 50)
    attempts = 0
    sc_list = get_list()
    player_name = input("Please enter your name: ")

    while True:
        guess = int(input("Guess the secret number (between 1 and 50): "))
        attempts += 1

        if guess == secret:
            game_res_obj = game_res(attempts=attempts, player_name=player_name, date=str(datetime.datetime.now()))

            sc_list.append(game_res_obj.__dict__)

            with open("scores.txt", "w") as score_file:
                score_file.write(json.dumps(sc_list))

            print("Welldone! It's number " + str(secret))
            print("Number of attempts: " + str(attempts))
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


def get_list():
    with open("scores.txt", "r") as score_file:
        sc_list = json.loads(score_file.read())
        return sc_list


def get_top_scores():
    score_list = get_list()
    tsc_list = sorted(score_list, key=lambda k: k["attempts"])[:3]
    return tsc_list
