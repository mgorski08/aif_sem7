#!/usr/bin/python3
import numpy as np


class Neuron:
    def __init__(self, weights, activation_function, inputs):
        self.weights = np.array(weights)
        self.activation_function = activation_function
        self.inputs = inputs

    def set_inputs(self, inputs):
        self.inputs = inputs

    def get_inputs(self):
        values = []
        for neuron_input in self.inputs:
            values.append(neuron_input())
        return np.array(values)

    def calculate(self):
        return self.calculate_raw(self.get_inputs())

    def calculate_raw(self, np_values):
        return self.activation_function(self.weights @ np_values)

    def activ_fun_derivative(self, x):
        dx = 0.00001
        return (self.activation_function(x+dx)-self.activation_function(x))/dx

    def calc_weight_update(self, learning_rate, expected_output):
        actual_output = self.calculate()
        error = expected_output-actual_output
        return learning_rate * error * self.activ_fun_derivative(self.weights @ self.get_inputs()) * self.get_inputs()

    def update_weights(self, weights_diff):
        self.weights += weights_diff

    def calc_and_update_weights(self, learning_rate, expected_output):
        self.update_weights(self.calc_weight_update(learning_rate, expected_output))
