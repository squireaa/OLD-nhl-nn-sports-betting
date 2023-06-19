# ====defines the function used to get the averages for the last n games=====
import pandas as pd
import os
import sys
from datetime import datetime
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.get_3let_code import get_three_letter_code

# function to add the 3 letter code key and pd.df value to the proper dictionary
def add_group_to_dict(dict, group):
    for g in group:
        lets = get_three_letter_code(g['Team'].iloc[0])
        dict[lets] = g

def add_lists(list1, list2):
    result = []
    for item1, item2 in zip(list1, list2):
        if not isinstance(item1, str) and not isinstance(item2, str):
            result.append(item1 + item2)
    return result

def remove_strings(lst):
    return [x for x in lst if not isinstance(x, str)]

# ========= START SECTION ==============
# creates dictionaries of {"ABC": pd.df, "DEF": pd.df} for each team and their advanced stats for each year
eighteen_dict = {}
nineteen_dict = {}
twenty_dict = {}
twenty_one_dict = {}
twenty_two_dict = {}

eighteen_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_2018.csv")
nineteen_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_2019.csv")
twenty_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_2020.csv")
twenty_one_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_2021.csv")
twenty_two_df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/nhl_dropped_2022.csv")

eighteen_group = [group for _, group in eighteen_df.groupby('Team')]
nineteen_group = [group for _, group in nineteen_df.groupby('Team')]
twenty_group = [group for _, group in twenty_df.groupby('Team')]
twenty_one_group = [group for _, group in twenty_one_df.groupby('Team')]
twenty_two_group = [group for _, group in twenty_two_df.groupby('Team')]

# add_group_to_dict(eighteen_dict, eighteen_group)
add_group_to_dict(nineteen_dict, nineteen_group)
add_group_to_dict(twenty_dict, twenty_group)
add_group_to_dict(twenty_one_dict, twenty_one_group)
add_group_to_dict(twenty_two_dict, twenty_two_group)

dicts_list = [eighteen_dict, nineteen_dict, twenty_dict, twenty_one_dict, twenty_two_dict]
year_order = [2018, 2019, 2020, 2021, 2022]
# ========= END SECTION ==============

def get_last_n(my_id: str, how_many: int) -> list:
    # define which dataset to look in
    season = int(my_id[4:8])

    # account for games occuring in oct-dec being different than the calendar year
    if int(my_id[9:11]) >= 10:
        season += 1

    # create a df with only the relevant data to the team and the year
    working_dict = dicts_list[year_order.index(season)]
    working_df = working_dict[my_id[:3]]

    # figure out what game number the given game is
    working_df = working_df.reset_index()
    index = working_df['Date'].tolist().index(my_id[4:]) - 1
    if index == -1:
        return [] * 62

    # average the values of the last n games
    start = working_df.iloc[index].values.tolist()
    added_list = add_lists(start, [0] * len(start))
    num_to_divide_by = 1
    for i in [index - j for j in range(1, how_many)]:
        if i < 0:
            continue
        num_to_divide_by += 1
        added_list = add_lists(remove_strings(working_df.iloc[i]), added_list)

    # return the list of averaged values
    return [round(x / num_to_divide_by, 4) for x in added_list]

'''
# THIS CAN BE USED TO CHECK FOR USAGE

print((get_last_n("EDM-2021-10-16", 3)))
working_dict = dicts_list[year_order.index(2022)]
working_df = working_dict["EDM"]
print(working_df)
'''


def get_rest_days(my_id: str) -> int:
    # define which dataset to look in
    season = int(my_id[4:8])

    # account for games occuring in oct-dec being different than the calendar year
    if int(my_id[9:11]) >= 10:
        season += 1

    # create a df with only the relevant data to the team and the year
    working_dict = dicts_list[year_order.index(season)]
    working_df = working_dict[my_id[:3]]

    # figure out what game number the given game is
    working_df = working_df.reset_index()
    index = working_df['Date'].tolist().index(my_id[4:])
    if index < 0:
        raise ValueError("Can't do this with first game of the season")
    last_game = working_df['Date'].iloc[index - 1]
    this_game = working_df['Date'].iloc[index]

    date_format = "%Y-%m-%d"
    date1 = datetime.strptime(last_game, date_format)
    date2 = datetime.strptime(this_game, date_format)

    delta = date2 - date1
    return delta.days


def get_year(my_id:str) -> int:
    return int(my_id[4:8])



