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
from X_get_arch_odds import *
from X_get_last_x import *
from X_get_ohe_players import *

columns = {}
num_columns = 6133
column_names = ['column_{}'.format(i) for i in range(num_columns)]
for column_name in column_names:
    columns[column_name] = []
X_df = pd.DataFrame(columns)

every_my_id = list()
for year in range(22, 23):
    df = pd.read_csv(
        f"C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_20{year}.csv")
    for i in range(len(df)):
        every_my_id.append(
            "{0}-{1}".format(get_three_letter_code(df['Team'].iloc[i]), df['Date'].iloc[i]))

def get_main_metrics(my_id:str) -> list:
    to_return = []
    to_return.extend(get_last_n(my_id, 1))
    to_return.extend(get_last_n(my_id, 3))
    to_return.extend(get_last_n(my_id, 5))
    to_return.extend(get_last_n(my_id, 10))
    to_return.extend(fill_ohe(my_id))
    to_return.extend([get_rest_days(my_id)])
    return to_return


index = 0
for i in range(0, len(every_my_id), 2):
    (get_main_metrics(every_my_id[i]))