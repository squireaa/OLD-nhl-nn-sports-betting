# =====gets the advanced data and saves it to csvs=====
import pandas as pd
import datetime
from random import randint
from time import sleep
import os


def get_adv_metrics(year:int, num_years:int) -> None:
    # create a list of all the years being scraped from
    year_list = [n for n in range(year, year - num_years, -1)]

    for i, year in enumerate(year_list):
        # creates a df based on the url given
        url = "https://www.hockey-reference.com/leagues/NHL_{0}_games.html".format(year)
        dfs = pd.read_html(url)
        df = dfs[0]

        # gets a list of all the dates in which a game was played
        dates = pd.to_datetime(df['Date'], format="%Y-%m-%d").dt.date
        dates = pd.Series(dates).drop_duplicates().tolist()

        # defines variables needed in the proceding loop
        nhl_url = ''
        end_date = dates[-1]
        output_path = "nhl_adv_data{0}.csv".format(year)

        # loops through each date to get the data for the games played on each date
        for j, date in enumerate(dates):
            # defines the url needed for the specific date
            nhl_url = f"https://www.naturalstattrick.com/teamtable.php?fromseason={year-1}{year}&thruseason={year-1}{year}&stype=2&sit=ev&score=all&rate=y&team=all&loc=B&gpf=410&fd={date}&td={date}"
            
            if (date <= end_date):
                # saves the advanced data to a df
                nhl_dfs = pd.read_html(nhl_url, index_col=0)
                nhl_df = nhl_dfs[0]

                # adds a date column to the df and saves it
                nhl_df['Date'] = date
                nhl_df.to_csv(output_path, mode='a', header= not os.path.exists(output_path), index = False)
                
                # times out for a range of time to try to prevent against blacklisting
                sleep(randint(10, 25))

                # displays the status of the scraping
                print("{0}/{1}: {2}/{3}".format(i+1, len(year_list), j+1, len(dates)))
    print("Done.")

get_adv_metrics(2018, 1)