from functions_and_classes import *

while True:
    selection = input("Do you want to: a) play a new game, b) see the best scores, or c) quit? ")

    if selection.lower() == "a":
        play()
    elif selection.lower() == "b":
        for sc_dict in get_top_scores():
            result_obj = game_res(attempts=sc_dict.get("attempts"),
                                player_name=sc_dict.get("player_name", "Anonymous"),
                                date=sc_dict.get("date"))

            print("Player: {name}; Attempts: {attempts}; Date: {date}".format(name=result_obj.player_name,
                                                                              attempts=result_obj.attempts,
                                                                              date=result_obj.date))
    else:
        break
