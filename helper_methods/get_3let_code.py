# ====converts full name to ABC code======
team_dict = {
    "Anaheim Ducks" : "ANA",
    "Arizona Coyotes" : "ARI",
    "Boston Bruins" : "BOS",
    "Buffalo Sabres" : "BUF",
    "Calgary Flames" : "CGY",
    "Carolina Hurricanes" : "CAR",
    "Chicago Blackhawks" : "CHI",
    "Colorado Avalanche" : "COL",
    "Columbus Blue Jackets" : "CBJ",
    "Dallas Stars" : "DAL",
    "Detroit Red Wings" : "DET",
    "Edmonton Oilers" : "EDM",
    "Florida Panthers" : "FLA",
    "Los Angeles Kings" : "LAK",
    "Minnesota Wild" : "MIN",
    "Montreal Canadiens": "MTL",
    "Nashville Predators" : "NSH",
    "New Jersey Devils" : "NJD",
    "New York Islanders" : "NYI",
    "New York Rangers" : "NYR",
    "Ottawa Senators" : "OTT",
    "Philadelphia Flyers" : "PHI",
    "Pittsburgh Penguins" : "PIT",
    "San Jose Sharks" : "SJS",
    "Seattle Kraken" : "SEA",
    "St. Louis Blues" : "STL",
    "Tampa Bay Lightning" : "TBL",
    "Toronto Maple Leafs" : "TOR",
    "Vancouver Canucks" : "VAN",
    "Vegas Golden Knights" : "VGK",
    "Washington Capitals" : "WSH",
    "Winnipeg Jets" : "WPG",

    "Pittsburgh": "PIT",
    "TampaBay": "TBL",
    "SeattleKraken": "SEA",
    "Vegas": "VGK",
    "NYRangers": "NYR",
    "Washington": "WSH",
    "Montreal": "MTL",
    "Toronto": "TOR",
    "Vancouver": "VAN",
    "Edmonton": "EDM",
    "Chicago": "CHI",
    "Colorado": "COL",
    "Winnipeg": "WPG",
    "Anaheim": "ANA",
    "Ottawa": "OTT",
    "Buffalo": "BUF",
    "Florida": "FLA",
    "NYIslanders": "NYI",
    "Carolina": "CAR",
    "Dallas": "DAL",
    "Arizona": "ARI",
    "Columbus": "CBJ",
    "Detroit": "DET",
    "NewJersey": "NJD",
    "Philadelphia": "PHI",
    "Minnesota": "MIN",
    "Boston": "BOS",
    "St.Louis": "STL",
    "Calgary": "CGY",
    "SanJose": "SJS",
    "Nashville": "NSH",
    "LosAngeles": "LAK"
}

def get_three_letter_code(full_name:str):
    try:
        return team_dict[full_name]
    except:
        if full_name[:5] == "Montr":
            return team_dict["Montreal Canadiens"]
        else:
            pass