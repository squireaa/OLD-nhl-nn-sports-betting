import pandas as pd
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.get_3let_code import get_three_letter_code
from helper_methods.ohe_players import one_hottify

def add_group_to_dict(dict, group):
    for g in group:
        lets = get_three_letter_code(g['Team'].iloc[0])
        dict[lets] = g

eighteen_dict = {}
nineteen_dict = {}
twenty_dict = {}
twenty_one_dict = {}
twenty_two_dict = {}

# eighteen_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2018.csv")
# nineteen_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2019.csv")
twenty_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2020.csv")
twenty_one_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2021.csv")
twenty_two_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_adv_data2022.csv")

# eighteen_group = [group for _, group in eighteen_df.groupby('Team')]
# nineteen_group = [group for _, group in nineteen_df.groupby('Team')]
twenty_group = [group for _, group in twenty_df.groupby('Team')]
twenty_one_group = [group for _, group in twenty_one_df.groupby('Team')]
twenty_two_group = [group for _, group in twenty_two_df.groupby('Team')]

# add_group_to_dict(eighteen_dict, eighteen_group)
# add_group_to_dict(nineteen_dict, nineteen_group)
add_group_to_dict(twenty_dict, twenty_group)
add_group_to_dict(twenty_one_dict, twenty_one_group)
add_group_to_dict(twenty_two_dict, twenty_two_group)

dicts_list = [twenty_dict, twenty_one_dict, twenty_two_dict]
year_order = [2020, 2021, 2022]


def get_last_one(my_id:str) -> pd.DataFrame:
    season = int(my_id[4:8])
    if int(my_id[9:11]) >= 10:
        season += 1
    working_dict = dicts_list[year_order.index(season)]
    working_df = working_dict[my_id[:3]]

    working_df = working_df.reset_index()
    index = working_df.loc[working_df['Date'] == my_id[4:]].index[0]
    print(index)    

print(get_last_one("WPG-2021-10-23"))


