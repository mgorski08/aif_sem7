#!/usr/bin/python3
from task1.visual import Visual
import numpy as np

class0 = []
class1 = []


def refresh():
    class0.clear()
    class1.clear()
    c0_modes = int(vis.modes_c0_entry.get())
    c1_modes = int(vis.modes_c1_entry.get())
    c0_ppm = int(vis.p_per_mode_c0_entry.get())
    c1_ppm = int(vis.p_per_mode_c1_entry.get())
    c0_spread = float(vis.spread_c0_entry.get())
    c1_spread = float(vis.spread_c1_entry.get())

    for _ in range(c0_modes):
        class0.extend(generate_mode(np.random.random(), np.random.random(), c0_spread, c0_ppm))
    for _ in range(c1_modes):
        class1.extend(generate_mode(np.random.random(), np.random.random(), c1_spread, c1_ppm))

    vis.canvas.delete("all")
    vis.draw_graticule(0.1, 0.1)
    vis.draw_points(class0, "blue")
    vis.draw_points(class1, "red")


def generate_mode(x, y, std_dev, n):
    retval = []
    for i in range(n):
        retval.append((np.random.normal(loc=x, scale=std_dev), np.random.normal(loc=y, scale=std_dev)))
    return retval


vis = Visual(refresh, 500)
vis.mainloop()
