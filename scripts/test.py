from nhlstats import list_games
from nhlstats import list_shifts
import pandas as pd
from nhlstats.formatters import csv
from format_team_name import get_three_letter_code

games = list_games(start_date="2017-10-04", end_date="2022-12-31")
teams_list = list()
for i, game in enumerate(games):
    date = game['date']
    team1 = game['away_team']
    team2 = game['home_team']
    game_id = str(game['game_id'])
    
    if get_three_letter_code(team1) != None and get_three_letter_code(team1) != None:
        teams_list.append([date, get_three_letter_code(team1), get_three_letter_code(team2), game_id])

df = pd.DataFrame(columns=['my_id', 'player_list'])
row_index = 0
print(teams_list[0])

gameid = teams_list[0][3]
shifts = pd.DataFrame(list_shifts(gameid))
print(shifts['team_abbreviation'])