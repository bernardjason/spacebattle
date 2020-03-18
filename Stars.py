from tkinter import *
import math
from Runtime import Runtime
from random import randint


class Stars:

    def __init__(self, canvas: Canvas, x, y):
        self.x = x
        self.y = y
        self.stars = 8
        self.points = list()
        for i in range(0, self.stars * 4, 4):
            xx = randint(0, Runtime.SCREEN_X / 4) * 3 + 100
            yy = randint(0, Runtime.SCREEN_Y / 4) * 3 + 100
            self.points.append(self.x + xx)
            self.points.append(self.y + yy)
            self.points.append(self.x + xx + 1)
            self.points.append(self.y + yy + 1)

        self.coords = self.points.copy()
        self.img = list()
        for i in range(0, self.stars * 4, 4):
            self.img.append(canvas.create_rectangle(self.points[i:i + 4], outline="white"))

    def render(self, canvas: Canvas, rotation, playerx, playery):
        i = 0
        r = math.radians(rotation)
        addx = playerx - Runtime.SCREEN_X / 2
        addy = playery - Runtime.SCREEN_Y / 2

        for x, y in zip(self.points[::2], self.points[1::2]):
            xx = x - playerx
            yy = y - playery
            self.coords[i] = xx * math.cos(r) + yy * math.sin(r) + playerx - addx
            self.coords[i + 1] = -xx * math.sin(r) + yy * math.cos(r) + playery - addy
            i = i + 2

        for i in range(0, self.stars * 4, 4):
            star = self.img[int(i / 4)]
            canvas.coords(star, self.coords[i:i + 4])
