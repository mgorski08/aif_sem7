#!/usr/bin/python3
import tkinter


class Visual:
    def __init__(self, refresh, size):
        self.refresh = refresh
        self.size = size
        self.root = tkinter.Tk()

        self.modes_c0_label = tkinter.Label(self.root, text="Number of modes (class 0)")
        self.modes_c0_entry = tkinter.Entry(self.root)
        self.modes_c1_label = tkinter.Label(self.root, text="Number of modes (class 1)")
        self.modes_c1_entry = tkinter.Entry(self.root)
        self.button = tkinter.Button(self.root, text='Refresh', command=self.refresh)
        self.canvas = tkinter.Canvas(self.root, width=size, height=size)

        self.modes_c0_label.grid(row=0, column=0)
        self.modes_c0_entry.grid(row=0, column=1)
        self.modes_c1_label.grid(row=1, column=0)
        self.modes_c1_entry.grid(row=1, column=1)
        self.button.grid(row=2, column=0, columnspan=2)
        self.canvas.grid(row=3, column=0, columnspan=2)

    def draw_point_raw(self, x, y, fill):
        self.canvas.create_oval(x - 1, y - 1, x + 2, y + 2, fill=fill, width=0)

    def draw_point(self, x, y, fill):
        self.draw_point_raw(self.size * x, self.size * (1-y), fill)

    def draw_points(self, points, fill):
        for point in points:
            self.draw_point(*point, fill=fill)

    def mainloop(self):
        self.root.mainloop()
