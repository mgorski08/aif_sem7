#!/usr/bin/python3
import random

from task3.visual import Visual
from task3.neuron import Network
import numpy as np

class0 = []
class1 = []

network = Network()
eta = 0.05


def tuple2hexcolor(x):
    return f'#{int(x[0] * 255):02x}{int(x[1] * 255):02x}{int(x[2] * 255):02x}'


def learn():
    for _, i in enumerate(range(200)):
        print(f"{int(i / 2)}%")
        for _ in range(10):
            train_network()
        vis_neuron()
        vis.canvas.update_idletasks()


def train_network():
    data = [(el, [0, 0, 1]) for el in class0] + [(el, [1, 0, 0]) for el in class1]
    random.shuffle(data)
    for sample, y in data:
        grad = np.array(y) - network.calculate(np.array(sample))
        network.backpropagate(grad)
        network.adjust(eta)


def vis_neuron():
    vis.canvas.delete("all")
    x = 0
    while x <= 1:
        y = 0
        while y <= 1:
            prediction = network.calculate(np.array([x, y]))
            vis.draw_point(x, y, tuple2hexcolor(prediction), size=2)
            y += 0.02
        x += 0.02

    draw_data()
    vis.draw_graticule(0.1, 0.1)


def draw_data():
    vis.draw_points(class0, "blue")
    vis.draw_points(class1, "red")


def refresh():
    class0.clear()
    class1.clear()

    c0_modes = int(vis.modes_c0_entry.get())
    c1_modes = int(vis.modes_c1_entry.get())
    c0_ppm = int(vis.p_per_mode_c0_entry.get())
    c1_ppm = int(vis.p_per_mode_c1_entry.get())

    for _ in range(c0_modes):
        spread = np.random.random() * 0.03 + 0.005
        class0.extend(generate_mode(np.random.random(), np.random.random(), spread, c0_ppm))
    for _ in range(c1_modes):
        spread = np.random.random() * 0.02 + 0.01
        class1.extend(generate_mode(np.random.random(), np.random.random(), spread, c1_ppm))

    vis.canvas.delete("all")
    draw_data()
    vis.draw_graticule(0.1, 0.1)


def generate_mode(x, y, std_dev, n):
    retval = []
    for _ in range(n):
        retval.append((np.random.normal(loc=x, scale=std_dev), np.random.normal(loc=y, scale=std_dev)))
    return retval


vis = Visual(refresh, learn, 500)
vis.mainloop()
