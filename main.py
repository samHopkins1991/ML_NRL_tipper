from SLP import Perceptron
import numpy as np
import sqlite3
import os
import csv
num_rounds = 1
num_teams = 16
num_stat_columns = 10 #0 counts
LEARNING_RATE = 0.15
EPOCH = 1000

raw_training_inputs = []
raw_labels = []
processed_inputs = []
processed_labels = []


def load_training_data():
    global raw_training_inputs
    global processed_inputs
    cwd = os.getcwd()
    db_loc = '/home/samh/code/DB'
    os.chdir(db_loc)
    con = sqlite3.connect('NRL_2021.db')
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM Ladder_1 ORDER BY ROWID'):
        raw_training_inputs.append(np.array(row))

    processed_inputs = np.delete(raw_training_inputs, 0, 1)

    for row in processed_inputs:
        processed_inputs = processed_inputs.astype(np.int64)
    return processed_inputs


def load_labels():
    global processed_labels
    global raw_labels
    cwd = os.getcwd()
    db_loc = '/home/samh/code/DB'
    os.chdir(db_loc)
    con = sqlite3.connect('NRL_2021.db')
    cur = con.cursor()

    for row in cur.execute('SELECT * FROM results_rd_1 ORDER BY ROWID'):
        raw_labels.append(np.array(row))

    processed_labels = np.delete(raw_labels, 0, axis=1)

    for row in processed_labels:
        processed_labels = processed_labels.astype(np.int64)
    return processed_labels


def load():
    load_training_data()
    load_labels()
    # print(processed_labels)
    # print(processed_inputs)


def t1():
    t1_confidence = 0.00
    team_inputs = []

    cwd = os.getcwd()
    db_loc = '/home/samh/code/DB'
    os.chdir(db_loc)
    con = sqlite3.connect('NRL_2021.db')
    cur = con.cursor()

    print("Enter the team name")
    team = input()
    sql_string = 'WHERE Team='+"'" + team +"'"
    print(sql_string)

    sql_team_input = '''
    SELECT Position, Matches, Wins, Losses, For, Against, Difference, Points, Away_Wins, Home_Losses 
    FROM Ladder_1 ''' + sql_string

    for row in cur.execute(sql_team_input):
        team_inputs.append(np.array(row))
    # print(team_inputs)
    prediction = perceptron_1.predict(team_inputs)[0]
    t1_confidence = perceptron_1.predict(team_inputs)[1]
    print(prediction)
    print(t1_confidence)
    return team, t1_confidence, prediction


def t2():
    t2_confidence = 0.00
    team_inputs = []

    cwd = os.getcwd()
    db_loc = '/home/samh/code/DB'
    os.chdir(db_loc)
    con = sqlite3.connect('NRL_2021.db')
    cur = con.cursor()

    print("Enter the team name")
    team = input()
    sql_string = 'WHERE Team='+"'" + team +"'"
    print(sql_string)

    sql_team_input = '''
    SELECT Position, Matches, Wins, Losses, For, Against, Difference, Points, Away_Wins, Home_Losses 
    FROM Ladder_1 ''' + sql_string

    for row in cur.execute(sql_team_input):
        team_inputs.append(np.array(row))
    prediction = perceptron_2.predict(team_inputs)[0]
    t2_confidence = perceptron_2.predict(team_inputs)[1]

    print(prediction)
    print(t2_confidence)
    return team, t2_confidence, prediction


def winning_team(t1_confidence, t2_confidence):
    if t1_confidence[1] > t2_confidence[1]:
        print("Predicted winner: " + t1_confidence[0])
        # print("Confidence Score: " + t1_confidence[1])

    elif t2_confidence[1] > t1_confidence[1]:
        print("Predicted winner: " + t2_confidence[0])


if __name__ == '__main__':

    load()
    perceptron_1 = Perceptron(num_stat_columns, EPOCH, LEARNING_RATE)
    perceptron_2 = Perceptron(num_stat_columns, EPOCH, LEARNING_RATE)
    perceptron_1.train(processed_inputs, processed_labels)
    perceptron_2.train(processed_inputs, processed_labels)
    winning_team(t1(), t2())







