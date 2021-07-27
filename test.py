import sqlite3
import numpy as np


round_no = int(input("What round are you entering?"))
prev_round = str(round_no - 1)

prev_ladder = "Ladder_" + str(round_no -1)
this_ladder = "Ladder_" + str(round_no)
this_results = "results_rd_" +str(round_no)

num_matches = int(input("How many matches were there this round?"))

prev_table = []
new_table = []

ext_cols = '''
             Away_Wins,
    Home_Losses,
    Home_Away,
    Prev_round
    '''
prev_ext_table = []

con = sqlite3.connect('nrl_2020.db')
cur = con.cursor()

new_sql_ladder = "CREATE TABLE Ladder_" + str(round_no)
new_sql_results = "CREATE TABLE results_rd_" + str(round_no)

ladder_command = new_sql_ladder + '''  (
    Team        TEXT    REFERENCES results_rd_1 (Teams),
    Position    INTEGER,
    Matches     INTEGER,
    Wins        INTEGER,
    Losses      INTEGER,
    [For]       INTEGER,
    Against     INTEGER,
    Difference  INTEGER,
    Points      INTEGER,
    Away_Wins   INTEGER,
    Home_Losses INTEGER,
    PRIMARY KEY (
        Team
    )
);'''

results_command = new_sql_results + '''(
    Team  TEXT    REFERENCES results_rd_1 (Team),
    Result INTEGER,
    PRIMARY KEY (
        Teams
    )
);'''

cols = '''(
    Team,
    Position,
    Matches,
    Wins,
    Losses,
    For,
    Against,
    Difference,
    Points,
    Away_Wins,
    Home_Losses,
    Home_Away,
    Prev_round)
    '''

teams = ['Knights',
        'Raiders',
        'Storm',
        'Wests Tigers',
        'Broncos',
        'Eels',
        'Panthers',
        'Rabbitohs',
        'Sharks',
        'Bulldogs',
        'Roosters',
        'Cowboys',
        'Dragons',
        'Sea Eagles',
        'Titans',
        'Warriors']
result = []

# create new ladder and results tables for this round
try:
    cur.execute(ladder_command)
except:
    print("Ladder_" + str(round_no) + " already exists")
try:
    cur.execute(results_command)
except:
    print("results_rd_" + str(round_no) + " already exists")


# bring the results from last week forward
if round_no > 1:
    for row in cur.execute(f'''SELECT * FROM results_rd_{prev_round}'''):
        result.append(np.array(row))

for x in range(len(result)):
    print(result[x][0])
    cur.execute(f'''
                UPDATE {this_ladder} SET Prev_round = {result[x][1]} WHERE Team ='{result[x][0]}'
                ''')
    con.commit()



for x in range(len(result)):
    ext_cols = '''
                 Away_Wins = 
        Home_Losses,
        Home_Away,
        Prev_round
        '''

    cur.execute(f'''UPDATE {this_ladder} SET {ext_cols}={row} WHERE Team ='{teams[x]}'
    ''')
    con.commit()

