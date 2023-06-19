# =====builds the spreadsheet to be used for the X data=====
from nhlstats import list_games
import pandas as pd
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.get_3let_code import get_three_letter_code
from helper_methods.ohe_players import one_hottify

games = list_games(start_date="2017-10-04", end_date="2022-12-31")
home_code = "{0}-{1}".format(get_three_letter_code(games[0]['home_team']), games[0]['date'])
away_code = "{0}-{1}".format(get_three_letter_code(games[0]['away_team']), games[0]['date'])

# will eventually need to include all 5 years
df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2022.csv")
my_id = "{0}-{1}".format(get_three_letter_code(df['Team'].iloc[0]), df['Date'].iloc[0])

# dont forget opp team data