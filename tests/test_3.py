import pytest
import pandas as pd
import ast
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
sys.path.append(parent_dir)
from scripts.X_get_arch_odds import *

# list all the games being checked
my_ids = ["NYR-2019-12-06", "NYI-2018-02-08", "ARI-2019-02-14", "NSH-2018-02-10", "COL-2018-11-21",
          "LAK-2018-02-20", "BOS-2022-01-04", "VGK-2021-05-08", "NYI-2020-09-17", "CGY-2019-03-15"]

# get the real data to check against
l1 = [[-110, 0], [109, 0], [6.5, 0, 1], [-110], [6.5, 0, 1], [-105], [1.5, 1], [-230]]
l2 = [[-133, 0], [-115, 0], [6, 1, 1], [-110], [6, 1, 1], [-105], [-1.5, 0], [240]]
l3 = [[135, 0], [141, 0], [5.5, 0, 1], [-110], [5.5, 0, 1], [-115], [1.5, 0], [-195]]
l4 = [[-143, 1], [-134, 1], [5.5, 1, 0], [100], [5.5, 1, 0], [100], [-1.5, 0], [210]]
l5 = [[-115, 1], [-125, 1], [5.5, 1, 1], [-110], [5.5, 1, 1], [-115], [-1.5, 1], [215]]
l6 = [[157, 1], [180, 1], [5.5, 1, 1], [-120], [5.5, 1, 1], [-120], [1.5, 1], [-154]]
l7 = [[-265, 1], [-300, 1], [5.5, 0, 0], [-115], [5.5, 0, 0], [-105], [-1.5, 1], [-120]]
l8 = [[-170, 1], [-216, 1], [5.5, 0, 1], [-110], [5.5, 0, 1], [105], [-1.5, 1], [110]]
l9 = [[134, 0], [155, 0], [5, 0, 1], [120], [5, 0, 1], [105], [1.5, 1], [-170]]
l10 = [[-300, 1], [-280, 1], [6, 0, 0], [-110], [6, 0, 0], [105], [-1.5, 1], [-114]]

exp_lists = [l1, l2, l3, l4, l5, l6, l7, l8, l9, l10]


# ensure the funcitons return the correct data
@pytest.mark.parametrize("my_id, exp_list", [
    ("NYR-2019-12-06", l1),
    ("NYI-2018-02-08", l2),
    ("ARI-2019-02-14", l3),
    ("NSH-2018-02-10", l4),
    ("COL-2018-11-21", l5),
    ("LAK-2018-02-20", l6),
    ("BOS-2022-01-04", l7),
    ("VGK-2021-05-08", l8),
    ("NYI-2020-09-17", l9),
    ("CGY-2019-03-15", l10)
])
def test_all_functions(my_id, exp_list):
    result_open_ml = get_open_ml(my_id)
    assert result_open_ml == exp_list[0]

    result_close_ml = get_close_ml(my_id)
    assert result_close_ml == exp_list[1]

    result_open_ou_line = get_open_ou_line(my_id)
    assert result_open_ou_line == exp_list[2]

    result_open_ou_odds = get_open_ou_odds(my_id)
    assert result_open_ou_odds == exp_list[3]

    result_close_ou_line = get_close_ou_line(my_id)
    assert result_close_ou_line == exp_list[4]

    result_close_ou_odds = get_close_ou_odds(my_id)
    assert result_close_ou_odds == exp_list[5]

    result_puck_line = get_puck_line(my_id)
    assert result_puck_line == exp_list[6]

    result_puck_line_odds = get_puck_line_odds(my_id)
    assert result_puck_line_odds == exp_list[7]
