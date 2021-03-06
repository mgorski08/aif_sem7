#!/usr/bin/python3
from task2.visual import Visual
from task2.neuron import Neuron
import numpy as np


class0 = []
class1 = []


def relu(x):
    if x < 0:
        return 0
    else:
        return x


neuron = Neuron([0.0, 0.0, 0.0], np.sin, None)


def to_lambda(iterable):
    return tuple((lambda: x for x in iterable))


def learn():
    for _ in range(50):
        for _ in range(50):
            train_neuron()
        vis_neuron()
        vis.canvas.update_idletasks()


def train_neuron():
    weight_update = np.array([0.0, 0.0, 0.0])
    neuron.set_inputs((lambda: 1, lambda: sample[0], lambda: sample[1]))
    for sample in class0:
        weight_update += neuron.calc_weight_update(0.07, 0)

    for sample in class1:
        weight_update += neuron.calc_weight_update(0.07, 1)

    weight_update /= (len(class0) + len(class1))
    neuron.update_weights(weight_update)


def vis_neuron():
    vis.canvas.delete("all")
    x = 0
    neuron.set_inputs((lambda: 1, lambda: x, lambda: y))
    while x <= 1:
        y = 0
        while y <= 1:
            if neuron.calculate() < 0.5:
                vis.draw_point(x, y, "blue", size=2)
            else:
                vis.draw_point(x, y, "red", size=2)
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
        spread = np.random.random()*0.03+0.005
        class0.extend(generate_mode(np.random.random(), np.random.random(), spread, c0_ppm))
    for _ in range(c1_modes):
        spread = np.random.random()*0.02+0.01
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
