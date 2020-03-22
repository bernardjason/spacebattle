from tkinter import *
import math
from Runtime import Runtime
import random

star_random_list_x = random.sample(range(10, Runtime.SCREEN_X-10), 200)
star_random_list_y = random.sample(range(10, Runtime.SCREEN_Y-10), 200)

class Stars:

    def __init__(self, canvas: Canvas, x, y):
        self.x = x
        self.y = y
        self.stars = 8
        self.points = [None] * self.stars * 4
        self.coords = self.points.copy()
        self.reset_points()
        self.img = list()
        for i in range(0, self.stars * 4, 4):
            self.img.append(canvas.create_rectangle(self.points[i:i + 4], outline="white"))

    def move_stars(self,x,y):
        self.x = x
        self.y = y
        self.reset_points()

    def reset_points(self):
        for i in range(0, self.stars * 4, 4):
            xx = star_random_list_x[i]
            yy = star_random_list_y[i]
            self.points[i] = (self.x + xx)
            self.points[i + 1] = (self.y + yy)
            self.points[i + 2] = (self.x + xx + 1)
            self.points[i + 3] = (self.y + yy + 1)

    def render(self, canvas: Canvas, rotation, playerx, playery,fps):
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
        return True
