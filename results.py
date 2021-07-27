import sqlite3
import numpy as np


# connect to sql db
round_no = int(input("What round are you entering?"))
prev_round = str(round_no - 1)

this_ladder = "Ladder_" + str(round_no)
this_results = "results_rd_" +str(round_no)

num_matches = int(input("How many matches were there this round?"))

prev_table = []
new_table = []

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
    cur.execut(f'''
                UPDATE {this_ladder} SET Away_Wins = {result[x]}
                ''')
    con.commit()

for x in range(len(result)):



for i in range(num_matches):
    print(f'Game {i+1}: ')
    home_team = input('Enter the home team')
    away_team = input('Enter the away team')
    winner = input('Enter the winner\n blank for a draw')

    if winner == home_team:
        # update results table with 1 for home_team 0 for away_team
        cur.execute(f'''UPDATE {this_results} SET Result = 0 WHERE Team ='{away_team}'          
                    ''')
        cur.execute(f'''UPDATE {this_results} SET Result = 1 WHERE Team ='{home_team}'          
                    ''')
        con.commit()
    elif winner == away_team:
        # update results table with 1 for away_team 0 for home_team
        cur.execute(f'''
        UPDATE {this_results} SET Result = 1 WHERE Team ='{away_team}'
                    ''')
        cur.execute(f'''UPDATE {this_results} SET Result = 0 WHERE Team ='{home_team}'
                    ''')
        # update ladder table with +1 for away wins for away_team
        cur.execute(f'''UPDATE {this_ladder} SET Home_Losses = Home_Losses +1 WHERE Team ='{home_team}'
                    ''')
        # update ladder table with +1 for home losses for home_team
        cur.execute(f'''UPDATE {this_ladder} SET Away_Wins = Away_Wins +1 WHERE Team ='{away_team}'
                   ''')

        con.commit()

    else:
        # Draw
        # update losses for both
        cur.execute(f'''
                    UPDATE {this_ladder} SET Losses = Losses +1 WHERE Team ='{home_team}'          
                    ''')
        cur.execute(f'''
                    UPDATE {this_ladder} SET Losses = Losses +1 WHERE Team ='{away_team}'          
                    ''')
        # update results for away_team and home_team with 0
        cur.execute(f'''UPDATE {this_results} SET Result = 0 WHERE Team ='{away_team}'   
                    ''')
        cur.execute(f'''UPDATE {this_results} SET Result = 0 WHERE Team ='{home_team}'
                    ''')
        # update ladder with home_losses with +1 for home_team
        cur.execute(f'''UPDATE {this_ladder} SET Home_Losses = Home_Losses +1 WHERE Team ='{home_team}'
                   ''')



