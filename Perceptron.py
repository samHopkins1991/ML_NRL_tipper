import csv
from SLP import Perceptron
import numpy as np

num_rounds = 1
num_teams = 16
num_stat_columns = 12  # 0 counts
LEARNING_RATE = 0.15
EPOCH = 1000

raw_training_inputs = []
raw_labels = []
processed_inputs = []
processed_labels = []


def load_training_data():
    global raw_training_inputs
    global processed_inputs


    with open('nrl_ladder_rd_1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)

        for row in reader:
            raw_training_inputs.append(np.array(row))

    processed_inputs = np.delete(raw_training_inputs, 0, 1)
    processed_inputs = np.delete(processed_inputs, 0, 0)

    for row in processed_inputs:
        processed_inputs = processed_inputs.astype(np.int64)

    return processed_inputs


def load_labels():
    global processed_labels
    global raw_labels


    with open('results_rd1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            raw_labels.append(np.array(row))

    processed_labels = np.delete(raw_labels, 0, axis=1)

    for row in processed_labels:
        processed_labels = processed_labels.astype(np.int64)

    return processed_labels


def t1():
    t1_confidence = 0.00
    team_inputs = []
    percep_input = []


    with open('nrl_ladder_rd_1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            team_inputs.append(np.array(row))


    print("Enter the team name")
    team = input()
    for row, stats in enumerate(team_inputs):
        if team in team_inputs[row][0]:
            percep_input.append(np.array(stats[1:]))

    percep_input = np.array(percep_input, dtype=float)

    prediction = perceptron_1.predict(percep_input)[0]
    t1_confidence = perceptron_1.predict(percep_input)[1]
    print(prediction)
    print(t1_confidence)
    return team, t1_confidence, prediction


def t2():
    t1_confidence = 0.00
    team_inputs = []
    percep_input = []

    with open('nrl_ladder_rd_1.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for row in reader:
            team_inputs.append(np.array(row))


    print("Enter the team name")
    team = input()
    for row, stats in enumerate(team_inputs):
        if team in team_inputs[row][0]:
            percep_input.append(np.array(stats[1:]))

    percep_input = np.array(percep_input, dtype=float)

    prediction = perceptron_2.predict(percep_input)[0]
    t2_confidence = perceptron_2.predict(percep_input)[1]

    print(prediction)
    print(t2_confidence)
    return team, t2_confidence, prediction


def winning_team(t1_confidence, t2_confidence):
    if t1_confidence[1] > t2_confidence[1]:
        print("Predicted winner: " + t1_confidence[0])
        # print("Confidence Score: " + t1_confidence[1])

    elif t2_confidence[1] > t1_confidence[1]:
        print("Predicted winner: " + t2_confidence[0])


def load():
    load_training_data()
    load_labels()
    # print(processed_labels)
    # print(processed_inputs)


if __name__ == '__main__':
    load()
    perceptron_1 = Perceptron(num_stat_columns, EPOCH, LEARNING_RATE)
    perceptron_2 = Perceptron(num_stat_columns, EPOCH, LEARNING_RATE)
    perceptron_1.train(processed_inputs, processed_labels)
    perceptron_2.train(processed_inputs, processed_labels)
    winning_team(t1(), t2())

