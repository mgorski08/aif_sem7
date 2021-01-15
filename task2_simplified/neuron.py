#!/usr/bin/python3
import numpy as np


class Neuron:
    def __init__(self, weights, activation_function, af_derivative):
        self.weights = np.array(weights)
        self.activation_function = activation_function
        self.af_derivative = af_derivative

    def calculate(self, inputs):
        return self.activation_function(self.weights @ inputs)

    def calc_weight_update(self, learning_rate, inputs, expected_output):
        actual_output = self.calculate(inputs)
        error = expected_output - actual_output
        return learning_rate * error * self.af_derivative(self.weights @ inputs) * inputs

    def update_weights(self, weights_diff):
        self.weights += weights_diff

    def calc_and_update_weights(self, learning_rate, inputs, expected_output):
        self.update_weights(self.calc_weight_update(learning_rate, inputs, expected_output))
