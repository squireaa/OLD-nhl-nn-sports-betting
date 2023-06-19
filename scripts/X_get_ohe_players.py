import pandas as pd
import ast
import sys
import os
from ordered_set import OrderedSet

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from helper_methods.ohe_players import one_hottify

df = pd.read_csv("C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/player_lists.csv")
df['player_list'] = df['player_list'].apply(ast.literal_eval)

player_set = OrderedSet()
for i in range(len(df)):
    l1 = list(df['player_list'].iloc[i])
    for player in l1:
        player_set.add(player)
player_set_list = list(player_set)

def fill_ohe(my_id:str) -> list:
    df2 = one_hottify(pd.DataFrame(), player_set_list)
    player_list = df[df['my_id'] == my_id]['player_list']
    for player in player_list:
        df2[player] = int(0)
        df2.loc[0, player] = int(1)
    df2 = df2.fillna(int(0))
    return df2.iloc[0].tolist()


print(fill_ohe("WPG-2017-10-04"))
fill_ohe("SJS-2017-10-05")