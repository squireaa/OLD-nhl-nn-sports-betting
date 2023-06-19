import pandas as pd
import os
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.get_3let_code import get_three_letter_code

df_2022 = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/2022odds.csv")
df_2021 = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/2021odds.csv")
df_2020 = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/2020odds.csv")
df_2019 = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/2019odds.csv")
df_2018 = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/2018odds.csv")
dfs_list = [df_2018, df_2019, df_2020, df_2021, df_2022]
year_order = [2018, 2019, 2020, 2021, 2022]

def get_open_ml(my_id:str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["Open"])
            if int(row["Final"]) > get_opp_score(my_id):
                l1.append(1) 
            else:
                l1.append(0)
    return l1


def get_close_ml(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["Close"])
            if int(row["Final"]) > get_opp_score(my_id):
                l1.append(1)
            else:
                l1.append(0)
    return l1


def get_close_ou_line(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["CloseOU"])
    return l1


def get_close_ou_odds(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["CloseOdds"])
            if int(row["Final"]) + int(get_opp_score(my_id)) > row["CloseOU"]:
                l1.append(1)
            else:
                l1.append(0)
    return l1


def get_open_ou_line(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["OpenOU"])
    return l1


def get_open_ou_odds(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["OpenOdds"])
    return l1


def get_puck_line(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["PL"])
    return l1


def get_puck_line_odds(my_id: str) -> list:
    l1 = []
    df = get_df(my_id)
    for index, row in df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            l1.append(row["PLOdds"])
    return l1

def get_df(my_id:str) -> pd.DataFrame:
    season = int(my_id[4:8])
    if int(my_id[9:11]) >= 10:
        season += 1
    df = dfs_list[year_order.index(season)]
    date = f"{my_id[9:11]}{my_id[12:]}"
    if date[0] == str(0):
        date = date[1:]
    return df[df["Date"] == int(date)]

def get_opp_score(my_id:str) -> int:
    season = int(my_id[4:8])
    if int(my_id[9:11]) >= 10:
        season += 1
    df = dfs_list[year_order.index(season)]
    date = f"{my_id[9:11]}{my_id[12:]}"
    if date[0] == str(0):
        date = date[1:]
    small_df = df[df["Date"] == int(date)]
    for index, row in small_df.iterrows():
        if get_three_letter_code(row["Team"]) == my_id[:3]:
            if (index % 2) == 0:
                return df["Final"].iloc[index + 1]
            return df["Final"].iloc[index - 1]
    raise ValueError("Something went wrong.")


print(get_close_ou_odds("EDM-2021-10-13"))