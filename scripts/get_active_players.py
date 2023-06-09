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

# ------------START LOOP SECTION---------------------------
for i in range(len(teams_list)):
    try:
        gameid = teams_list[i][3]
        player_list = set()
        team1_list = []
        team2_list = []

        shifts = pd.DataFrame(list_shifts(gameid))

        for j in range(len(shifts)):
            player_code = "{2} {0} {1}".format(shifts['first_name'][j], shifts['last_name'][j], shifts['team_abbreviation'][j])
            player_list.add(player_code)

        sorted_list = list(player_list)
        sorted_list.sort()

        for name in sorted_list:
            team1_letters = sorted_list[0][:3]
            if name[:3] == team1_letters:
                team1_list.append(name)
            else:
                team2_list.append(name)

        if str(teams_list[i][1]) == str(team1_letters):
            df.at[row_index, 'my_id'] = "{0}-{1}".format(teams_list[i][1], teams_list[i][0])
            df.at[row_index, 'player_list'] = team1_list
            row_index += 1
            df.at[row_index, 'my_id'] = "{0}-{1}".format(teams_list[i][2], teams_list[i][0])
            df.at[row_index, 'player_list'] = team2_list
            row_index += 1
        else:
            df.at[row_index, 'my_id'] = "{0}-{1}".format(teams_list[i][2], teams_list[i][0])
            df.at[row_index, 'player_list'] = team1_list
            row_index += 1
            df.at[row_index, 'my_id'] = "{0}-{1}".format(teams_list[i][1], teams_list[i][0])
            df.at[row_index, 'player_list'] = team2_list
            row_index += 1
    except:
        pass
    
    print("{0}/{1}".format(i, len(teams_list)))

df.to_csv("player_lists.csv")