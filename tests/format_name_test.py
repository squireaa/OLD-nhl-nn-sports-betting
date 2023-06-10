from nhlstats import list_games
from nhlstats import list_shifts
import pandas as pd
from nhlstats.formatters import csv
import sys
import os

sys.path.append("../scripts/")
from HELPER_three_let_code import get_three_letter_code

games = list_games(start_date="2017-10-04", end_date="2022-12-31")
teams_list = set()
for i, game in enumerate(games):
    date = game['date']
    team1 = game['away_team']
    team2 = game['home_team']
    game_id = game['game_id']

    teams_list.add(get_three_letter_code(team1))

df = pd.read_csv(
    "C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/2022odds.csv")

for i in range(200):
    team = df['Team'].iloc[i]
    teams_list.add(get_three_letter_code(team))

teams_list.discard(None)
print(len(teams_list))
