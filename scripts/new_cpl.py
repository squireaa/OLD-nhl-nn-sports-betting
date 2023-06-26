from nhlstats import list_games
from nhlstats import list_shifts
import pandas as pd
from nhlstats.formatters import csv
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.get_3let_code import get_three_letter_code

df = pd.read_csv("data/game_skater_stats.csv")
player_set = set()
for index, row in df.iterrows():
    player_set.add(int(row['player_id']))

print(player_set)
print(len(player_set))