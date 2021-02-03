#!/usr/bin/python3
import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def der(f):
    if f == sigmoid:
        return lambda x: sigmoid(x) * (1 - sigmoid(x))
    else:
        raise Exception("unsupported operation")


class Layer:
    pass


class Linear(Layer):
    def __init__(self, ninputs, width):
        self.w = np.random.rand(ninputs+1, width)

    def forward(self, x):
        self.x = x
        return np.array([*self.x, 1]) @ self.w

    def backward(self, grad):
        self.grad = grad
        return self.grad @ np.transpose(self.w)

    def adjust(self, eta):
        self.w += eta * np.array([*self.x, 1])[np.newaxis, :].T @ self.grad[np.newaxis, :]


class Activation(Layer):
    def __init__(self, f):
        self.f = f

    def forward(self, s):
        self.s = s
        return self.f(s)

    def backward(self, grad):
        return der(self.f)(self.s) * grad[:-1]

    def adjust(self, eta):
        pass


class Network:
    def __init__(self):
        self.layers = [Linear(2, 5), Activation(sigmoid),
                       Linear(5, 5), Activation(sigmoid),
                       Linear(5, 2), Activation(sigmoid)]

    def calculate(self, x):
        for layer in self.layers:
            x = layer.forward(x)
        return x

    def backpropagate(self, grad):
        grad = np.array([*grad, 0])
        for layer in self.layers[::-1]:
            grad = layer.backward(grad)

    def adjust(self, eta):
        for layer in self.layers:
            layer.adjust(eta)
