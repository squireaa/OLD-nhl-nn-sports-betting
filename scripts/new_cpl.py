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

# create a list of dictionaries of all games played between these dates
games = list_games(start_date="2017-10-04", end_date="2022-12-31")

# list will be format of [[date, "ABC", "DEF", ABC-yyyy-mm-dd], [date, "ABC", "DEF", DEF-yyyy-mm-dd], ...]
teams_list = list()

df2 = pd.DataFrame(columns=['my_id', 'player_list'])
row_index = 0

every_my_id = list()
for year in range(18, 23):
    df = pd.read_csv(
        f"C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_20{year}.csv")
    for i in range(len(df)):
        every_my_id.append(
            "{0}-{1}".format(get_three_letter_code(df['Team'].iloc[i]), df['Date'].iloc[i]))

for i in range(7314, len(every_my_id)):
    every_player = set()
    game_id = games[i]['game_id']
    shifts = pd.DataFrame(list_shifts(game_id))
    
    for j in range(len(shifts)):
        let3 = every_my_id[i][:3]
        first_name = shifts['first_name'][j]
        last_name = shifts['last_name'][j]
        player = f"{let3}-{first_name}-{last_name}"
        every_player.add(player)
    player_list_str = ', '.join(every_player)
    new_row = pd.DataFrame({'my_id': every_my_id[i], 'player_list': str(player_list_str)}, index=[0])
    df2 = pd.concat([df2, new_row], ignore_index=True)
    print(f"{i}/{len(every_my_id)}")

    df2.to_csv("player_lists1.csv")
