from sbrscrape import Scoreboard
import pandas as pd
games = Scoreboard(sport="NHL").games[0] # see note at bottom

def get_odds(sb: str) -> dict:
    # sb = sportsbook
    if sb not in ['betmgm', 'draftkings', 'fanduel', 'pointsbet', 'wynn', 'bet_rivers_ny']:
        raise KeyError("Sportsbook '{0}' not found.".format(sb))
    return {'home-team': games['home_team'], 'away-team': games['away_team'],
            'uo-total': games['total'][sb], 'under-odds': games['under_odds'][sb],
            'over-odds': games['over_odds'][sb], 'home-ml': games['home_ml'][sb],
            'away-ml': games['away_ml'][sb]}

dk_sb = get_odds('draftkings')
print(dk_sb)

# will eventaully need to iterate through .games[n] when there is more than just one game (finals)