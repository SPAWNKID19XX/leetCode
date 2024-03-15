import unittest
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

def get_score(game_stamps, offset):
    '''
    Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
    Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    current_stamp = game_stamps
    while len(current_stamp) > 1:
        if current_stamp[int(len(current_stamp)/2)]['offset'] > offset:
            current_stamp = current_stamp[:int(len(current_stamp)/2)]
        else:
            current_stamp = current_stamp[int(len(current_stamp)/2):]
    if current_stamp[0]['offset'] == offset:
        return f"At offset {offset}, Home Score: {current_stamp[0]['score']['home']}, Away Score: {current_stamp[0]['score']['away']}"
    else:
        return 'Offset does not exist'

game_stamps = generate_game()
pprint(game_stamps)
game_score = get_score(game_stamps, 1000)
print(game_score)

class TestGetScoreFunction(unittest.TestCase):

    def setUp(self):
        self.game_stamps = generate_game()
        self.game_score = get_score(self.game_stamps, 1000)

    def test_stamp_exist(self):
        self.assertIsNotNone(self.game_stamps)

    def test_offset_exist(self):
        offset_exists = any('offset' in stamp for stamp in self.game_stamps)
        self.assertTrue(offset_exists, "Offset exists in game stamps")

    def test_game_score_not_none(self):
        self.assertIsNotNone(self.game_score)



if __name__ == '__main__':
    unittest.main()
