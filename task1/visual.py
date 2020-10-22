#!/usr/bin/python3
import tkinter


class Visual:
    def __init__(self, refresh, size):
        self.refresh = refresh
        self.size = size
        self.root = tkinter.Tk()

        tkinter.Label(self.root, text="Number of modes").grid(row=0, column=1)
        tkinter.Label(self.root, text="Points per mode").grid(row=0, column=2)
        tkinter.Label(self.root,          text="Spread").grid(row=0, column=3)

        tkinter.Label(self.root,         text="Class 0").grid(row=1, column=0)
        tkinter.Label(self.root,         text="Class 1").grid(row=2, column=0)

        self.modes_c0_entry = tkinter.Entry(self.root)
        self.modes_c1_entry = tkinter.Entry(self.root)
        self.p_per_mode_c0_entry = tkinter.Entry(self.root)
        self.p_per_mode_c1_entry = tkinter.Entry(self.root)
        self.spread_c0_entry = tkinter.Entry(self.root)
        self.spread_c1_entry = tkinter.Entry(self.root)

        self.button = tkinter.Button(self.root, text='Refresh', command=self.refresh)
        self.canvas = tkinter.Canvas(self.root, width=size, height=size)

        self.modes_c0_entry.grid(row=1, column=1)
        self.modes_c1_entry.grid(row=2, column=1)
        self.p_per_mode_c0_entry.grid(row=1, column=2)
        self.p_per_mode_c1_entry.grid(row=2, column=2)
        self.spread_c0_entry.grid(row=1, column=3)
        self.spread_c1_entry.grid(row=2, column=3)
        self.button.grid(row=3, column=0, columnspan=4)
        self.canvas.grid(row=4, column=0, columnspan=4)

    def draw_point_raw(self, x, y, fill):
        self.canvas.create_oval(x - 1, y - 1, x + 2, y + 2, fill=fill, width=0)

    def draw_point(self, x, y, fill):
        self.draw_point_raw(self.size * x, self.size * (1-y), fill)

    def draw_points(self, points, fill):
        for point in points:
            self.draw_point(*point, fill=fill)

    def mainloop(self):
        self.root.mainloop()
