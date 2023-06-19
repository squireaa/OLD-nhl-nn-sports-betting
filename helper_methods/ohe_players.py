#====one hot encode the player names======
import pandas as pd

def one_hottify(df:pd.DataFrame, player_set:set) -> pd.DataFrame:
    # idk wtf this does chatgpt helped me on this part
    encoded_columns = [pd.Series([int(item in player_set) for _ in range(
        len(df))], dtype='int') for item in player_set]

    df_encoded = pd.concat(encoded_columns, axis=1)
    df_encoded.columns = player_set
    return df_encoded
