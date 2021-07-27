import numpy as np
import sqlite3

round_ladder = []
final_ladder = []

def xyz_array():
    global round_ladder
    global final_ladder
    con = sqlite3.connect('nrl_2020.db')
    cur = con.cursor()
    rounds = 2

    for x in range(rounds):
        for row in cur.execute(f'SELECT * FROM Ladder_{x+1}'):
            round_ladder.append(np.array(row))

        final_ladder.append(np.array(round_ladder))
        print('***Round Ladder**')
        print(round_ladder)
        print()
        print('**Final LAdder**')
        print(final_ladder)

        round_ladder.clear()
        z_array = final_ladder
    return z_array


xyz_array()

print(final_ladder[1])

# print(xyz_array()[1][0])