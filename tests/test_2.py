import pandas as pd
import ast
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# Add the parent directory to the system path
sys.path.append(parent_dir)

# import get_three_letter_code from HELPER_three_let_code
from helper_methods.ohe_players import one_hottify

df = pd.read_csv(
    "C:/Users/Owner/Desktop/cs stuff/Open Source/nhl-nn-sports-betting/data/player_lists.csv")
df['player_list'] = df['player_list'].apply(ast.literal_eval)

player_set = set()
for i in range(len(df)):
    l1 = list(df['player_list'].iloc[i])
    for player in l1:
        player_set.add(player)

df2 = pd.DataFrame()
one_hottify(df2, player_set)
print(df2)
