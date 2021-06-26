import sqlite3
import numpy as np

# connect to sql db
round_no = int(input("What round are you entering?"))
prev_round = str(round_no - 1)

this_ladder = "Ladder_" + str(round_no)


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
    Teams  TEXT    REFERENCES results_rd_1 (Teams),
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

teams = []


# create new ladder and results tables for this round
try:
    cur.execute(ladder_command)
except:
    print("Ladder_" + str(round_no) + " already exists")
try:
    cur.execute(results_command)
except:
    print("results_rd_" + str(round_no) + " already exists")

# load data from previous round
for row in cur.execute("SELECT * FROM Ladder_" + prev_round + " ORDER BY ROWID"):
    teams.append(row[0])
    prev_table.append(np.array(row))

for x in range(len(teams)):
    team_string = " "
    cat_str = team_string + teams[x] + "'"
    string = f'''INSERT INTO Ladder_{str(round_no)} {cols} SELECT * FROM Ladder_{prev_round}
     WHERE Team='{teams[x]}\''''
    print(string)
    cur.execute(string)
    con.commit()


for i in range(num_matches):
    home_team = input('Enter the home team')
    home_score = input("Enter their score")
    away_team = input('Enter the away team')
    away_score = input('Enter the away score')

    if home_score > away_score:
        # update results table with 1 for home_team 0 for away_team
        print("lol")
    elif away_score > home_score:
        # update results table with 1 for away_team 0 for home_team
        # cur.execute
        # update ladder table with +1 for away wins for away_team
        cur.execute(f'''UPDATE {this_ladder} SET Home_Losses = Home_Losses +1 WHERE TEAM ='{away_team}''')
        # update ladder table with +1 for home losses for home_team

        cur.execute(f'''UPDATE {this_ladder} SET Home_Losses = Home_Losses +1 WHERE TEAM ='{home_team}'
                   ''')
        con.commit()

    else:
        print("lol")
        # Draw
        # update results for away_team and home_team with 0
        # update ladder with home_losses with +1 for home_team


#
#
#
#
# cur.execute("SELECT * INTO Ladder_" + str(round_no) + " FROM Ladder_" + prev_round)
# print(new_table[0][0])
# num_matches = input("How many matches were there this round")
#

#         cur.execute("UPDATE")
