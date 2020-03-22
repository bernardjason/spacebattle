from tkinter import *
from Asteroid import Asteroid
import math


class Radar:

    def __init__(self, canvas: Canvas, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.img = canvas.create_rectangle(x, y, x + size, y + size, outline="white")
        self.img = canvas.create_rectangle(x, y, x + size, y + size, outline="white")
        middlex = 8
        middley = 8
        self.middle = int(self.size / 2)
        self.points = [self.x + self.middle - middlex, self.y + self.middle - middley,
                       self.x + self.middle, self.y + self.middle + middley,
                       self.x + self.middle + middlex, self.y + self.middle - middley]
        self.coords = self.points.copy()
        self.player = canvas.create_polygon(self.points, outline="white")
        self.front = canvas.create_rectangle(self.points[2] - 2, self.points[3] - 2, self.points[2] + 2,
                                             self.points[3] + 2, fill="pink")
        self.show = list()

    def render(self, canvas: Canvas, rotation):
        i = 0
        r = math.radians(180 - rotation)

        for x, y in zip(self.points[::2], self.points[1::2]):
            xx = x - self.middle - self.x
            yy = y - self.middle - self.y
            self.coords[i] = xx * math.cos(r) + yy * math.sin(r) + self.middle + self.x
            self.coords[i + 1] = -xx * math.sin(r) + yy * math.cos(r) + self.middle + self.y
            i = i + 2

        canvas.coords(self.player, self.coords)
        canvas.coords(self.front, self.coords[2] - 2, self.coords[3] - 2, self.coords[2] + 2, self.coords[3] + 2)

    def reset(self,canvas:Canvas):
        for i in self.show:
            canvas.delete(i)
        self.show.clear()


    def update(self, canvas: Canvas, x, y, rotation, asteroids):
        self.render(canvas, rotation)
        a: Asteroid
        scale = self.size /8

        self.reset(canvas)

        for a in asteroids:
            xx = (a.x - x) / scale
            yy = (a.y - y) / scale
            if xx > -self.middle and xx < self.middle and yy > -self.middle and yy < self.middle:
                xx = xx + self.x + self.middle
                yy = yy + self.middle + self.y
                point = canvas.create_rectangle(xx, yy, xx + 5, yy + 9, fill="yellow")
                self.show.append(point)
