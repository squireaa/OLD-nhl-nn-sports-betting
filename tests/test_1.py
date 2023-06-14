from nhlstats import list_games
from nhlstats import list_shifts
import pandas as pd
from nhlstats.formatters import csv
import sys
import os

# Get the parent directory of the current script and include in Python module search path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the system path
sys.path.append(parent_dir)

#import get_three_letter_code from HELPER_three_let_code
from scripts.HELPER_three_let_code import get_three_letter_code


games = list_games(start_date="2017-10-04", end_date="2022-12-31")
teams_list = set()
for i, game in enumerate(games):
    date = game['date']
    team1 = game['away_team']
    team2 = game['home_team']
    game_id = game['game_id']

    teams_list.add(get_three_letter_code(team1))

# beacuse the Python search path contains path for the parent folder (nhl-nn-sports-betting) 
df = pd.read_csv("data/2022odds.csv")

for i in range(200):
    team = df['Team'].iloc[i]
    teams_list.add(get_three_letter_code(team))

teams_list.discard(None)
print(teams_list)
print(len(teams_list))
