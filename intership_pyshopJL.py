from pprint import pprint
import random
import math

TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1
    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)
    return stamps

game_stamps = generate_game()

pprint(game_stamps)


def get_score(game_stamps, offset):
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.

        Принимает список штампов игры и временное смещение, для которого возвращает счет для домашней и гостевой команд. 
        Обратите внимание, что для некоторых смещений список штампов игры может не содержать счета.

    '''  
    curent_stamp = game_stamps
    while len(curent_stamp) > 1:
        if curent_stamp[int(len(curent_stamp)/2)]['offset'] > offset:
            curent_stamp = curent_stamp[:int(len(curent_stamp)/2)]
        else:
            curent_stamp = curent_stamp[int(len(curent_stamp)/2):]
    if curent_stamp[0]['offset'] == offset:
        return f"At offset {offset}, Home Score: {curent_stamp[0]['score']['home']}, Away Score: {curent_stamp[0]['score']['away']}"
    else:
        return 'Offset does not exist'

get_score = get_score(game_stamps, 1000)
print(get_score)

    
