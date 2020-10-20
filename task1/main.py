#!/usr/bin/python3
from task1.visual import Visual
import numpy as np

class0 = []

def refresh():
    vis.draw_points(generate_mode(0, 0, 0.02, 50000), "green")


def generate_mode(x, y, std_dev, n):
    retval = []
    for i in range(n):
        retval.append((np.random.normal(loc=x, scale=std_dev), np.random.normal(loc=y, scale=std_dev)))
    return retval


vis = Visual(refresh, 500)
vis.mainloop()
