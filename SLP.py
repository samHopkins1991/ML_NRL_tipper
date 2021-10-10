import numpy as np


class Perceptron(object):
    def __init__(self, no_inputs, epoch, learning_rate):
        self.epoch = epoch
        self.learning_rate = learning_rate
        self.weights = np.zeros(no_inputs + 1)
        self.weights = self.weights.astype(float)

    def predict(self, inputs):
        summation = np.dot(inputs, self.weights[1:]) + self.weights[0]
        if summation > 0:
            activation = 1
        else:
            activation = 0
        return activation, summation

    def train(self, training_inputs, labels):
        for _ in range(self.epoch):
            for inputs, label in zip(training_inputs, labels):
                prediction = self.predict(inputs)[0]
                self.weights[1:] += self.learning_rate * (label - prediction) * inputs
                self.weights[0] += self.learning_rate * (label - prediction)


