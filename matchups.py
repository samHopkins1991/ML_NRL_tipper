import numpy as np
import sqlite3

con = sqlite3.connect('nrl_2020.db')
cur = con.cursor()

round_no = int(input("What round are you entering?"))
num_matches = int(input("How many matches were there this round?"))
this_ladder = "Ladder_" + str(round_no)

for i in range(num_matches):
    print(f'Game {i +1}:')
    home_team = input('Enter the home team')
    away_team = input('Enter the away team')

    cur.execute(f'''UPDATE {this_ladder} SET Home_away = 1 WHERE Team ='{home_team}'
                ''')
    cur.execute(f'''UPDATE {this_ladder} SET Home_away = 0 WHERE Team ='{away_team}'
                    ''')
    con.commit()
