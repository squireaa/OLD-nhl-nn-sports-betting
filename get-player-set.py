from nhlstats import list_games
from nhlstats import list_shifts
import pandas as pd
from nhlstats.formatters import csv
import pickle

game_ids = []
all_players = set()
games = list_games(start_date="2017-10-04", end_date="2022-12-31")
for game in games:
    game_ids.append(game['game_id'])

for i, game_id in enumerate(game_ids):
    shifts = pd.DataFrame(list_shifts(game_id))
    for j in range(len(shifts)):
        all_players.add("{0} {1} {2}".format(
            shifts['team_abbreviation'][j], shifts['first_name'][j], shifts['last_name'][j]))
    print("{0}/{1}".format(i+1, len(game_ids)))

print(len(all_players))

with open('player_set.pkl', 'wb') as file:
    pickle.dump(all_players, file)
