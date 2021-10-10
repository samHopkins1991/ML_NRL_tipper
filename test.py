import sqlite3
import numpy as np
from icecream import ic
import os

db_loc = '/home/samh/code/python/nrl_2020'
os.chdir(db_loc)

round_no = int(input("What round are you entering?"))
prev_round = str(round_no - 1)

prev_ladder = "Ladder_" + str(round_no -1)
this_ladder = "Ladder_" + str(round_no)
this_results = "results_rd_" +str(round_no)

num_matches = int(input("How many matches were there this round?"))

prev_table_short = []
new_table = []
result = []
prev_ext_table = []


ext_cols = '''
             Away_Wins,
    Home_Losses,
    Home_Away,
    Prev_round
    '''

other_cols = '''
             Wins,
            Losses,
            Away_Wins,
            Home_Losses,
            Home_Away
            '''

short_cols = '''
            Team,
            Wins,
            Losses,
            Away_Wins,
            Home_Losses,
            Home_Away
            '''
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
    Home_Away   INTEGER,
    Prev_round  INTEGER,
    PRIMARY KEY (
        Team
    )
);'''

results_command = new_sql_results + '''(
    Team  TEXT    REFERENCES results_rd_1 (Team),
    Result INTEGER,
    PRIMARY KEY (
        Team
    )
);'''

cols = '''
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
    Prev_round
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

insert_command = '''INSERT '''
# create new ladder and results tables for this round
try:
    cur.execute(ladder_command)
except:
    print("Ladder_" + str(round_no) + " already exists")


try:
    cur.execute(results_command)
except:
    print("results_rd_" + str(round_no) + " already exists")



# This brings forward wins, losses away wins, home losses, home_away
# Becuase they are updated in other scripts. Other ladder info will be dropped in through sqlite studio

if round_no > 1:
    print(f"SELECT {short_cols} FROM {prev_ladder}")
    for row in cur.execute(f"SELECT {short_cols} FROM {prev_ladder}"):
        prev_table_short.append(np.array(row))

##for loop length of teams
## inner loop loops through cols to update, with values from

cols = ['Wins',
        'Losses',
        'Away_Wins',
        'Home_Losses',
        'Home_Away']
values = []
for x in range(len(prev_table_short)):
    values.append(np.array(prev_table_short[x][1:]))

for x in range(len(teams)):
    for col in range(len(cols)):
        print(prev_table_short[x])
        print(f'UPDATE {this_ladder} SET {cols[col]} = {values[x][col]} WHERE Team = {prev_table_short[x][0]}')
        cur.execute(f'''
        UPDATE {this_ladder} SET {cols[col]} = {values[x][col]} WHERE Team ='{prev_table_short[x][0]}'
                    ''')
        con.commit()


## this should be done - need to use results.py to update custom metrics.
## inputting matchups will update home_away

# prints the whole team row
print(prev_table_short[0])

# prints everything except the name
print(prev_table_short[0][1:])

#prints just the name of the team
print(prev_table_short[0][0])



# this executes inserting the whole table
# cur.executemany(f"INSERT INTO {this_ladder} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", prev_table)








