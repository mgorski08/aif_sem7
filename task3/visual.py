#!/usr/bin/python3
import tkinter


class Visual:
    def __init__(self, refresh, learn, size):
        self.size = size
        self.root = tkinter.Tk()

        tkinter.Label(self.root, text="Number of modes").grid(row=0, column=1)
        tkinter.Label(self.root, text="Points per mode").grid(row=0, column=2)

        tkinter.Label(self.root, text="Class 0").grid(row=1, column=0)
        tkinter.Label(self.root, text="Class 1").grid(row=2, column=0)

        self.modes_c0_entry = tkinter.Entry(self.root)
        self.modes_c1_entry = tkinter.Entry(self.root)
        self.p_per_mode_c0_entry = tkinter.Entry(self.root)
        self.p_per_mode_c1_entry = tkinter.Entry(self.root)

        self.modes_c0_entry.insert(0, 3)
        self.modes_c1_entry.insert(0, 5)
        self.p_per_mode_c0_entry.insert(0, 20)
        self.p_per_mode_c1_entry.insert(0, 20)

        self.refresh_button = tkinter.Button(self.root, text='Refresh', command=refresh)
        self.learn_button = tkinter.Button(self.root, text='Learn', command=learn)
        self.canvas = tkinter.Canvas(self.root, width=size, height=size)

        self.modes_c0_entry.grid(row=1, column=1)
        self.modes_c1_entry.grid(row=2, column=1)
        self.p_per_mode_c0_entry.grid(row=1, column=2)
        self.p_per_mode_c1_entry.grid(row=2, column=2)
        self.refresh_button.grid(row=3, column=0)
        self.learn_button.grid(row=3, column=1)
        self.canvas.grid(row=4, column=0, columnspan=3)
        self.draw_graticule(0.1, 0.1)

    def draw_point_raw(self, x, y, fill, size=3):
        self.canvas.create_oval(x - (size+1), y - (size+1), x + size, y + size, fill=fill, width=0)

    def draw_point(self, x, y, fill, **kwargs):
        self.draw_point_raw(*self.unit2canvas_size((x, y)), fill, **kwargs)

    def draw_points(self, points, fill, **kwargs):
        for point in points:
            self.draw_point(*point, fill=fill, **kwargs)

    def draw_line(self, x1, y1, x2, y2, **kwargs):
        self.canvas.create_line(*self.unit2canvas_size((x1, y1)), *self.unit2canvas_size((x2, y2)), **kwargs)

    def mainloop(self):
        self.root.mainloop()

    def unit2canvas_size(self, xy):
        x, y = xy
        return (self.size * (x*0.9+0.05)), self.size * (1 - (y*0.9+0.05))

    def draw_graticule(self, dx, dy):
        x = 0
        while x < 1:
            self.draw_line(x, 0, x, 1, dash=(1, 2))
            x += dx

        y = 0
        while y < 1:
            self.draw_line(0, y, 1, y, dash=(1, 2))
            y += dy
