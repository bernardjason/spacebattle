from tkinter import *
import math
import Runtime
from random import randint
from random import random


class Asteroid:

    def __init__(self, canvas: Canvas, x, y, size):
        self.x = x
        self.y = y
        self.movex = randint(-1, 1) * random() / 2
        self.movey = randint(-1, 1) * random() / 2
        self.centre_x = 10 * size / 2
        self.centre_y = 12 * size / 2
        self.size = size
        self.set_points()
        self.coords = self.points.copy()
        self.img = canvas.create_polygon(self.points, fill='', outline="yellow", width=3)

    def set_points(self):
        self.points = [self.x, self.y + 5 * self.size,
                       self.x + 10 * self.size, self.y + 8 * self.size,
                       self.x + 10 * self.size, self.y - 8 * self.size,
                       self.x - 4 * self.size, self.y - 10 * self.size,
                       self.x - 16 * self.size, self.y - 2 * self.size,
                       self.x - 4 * self.size, self.y + 6 * self.size
                       ]

    def render(self, canvas: Canvas, rotation, playerx, playery):
        i = 0
        r = math.radians(rotation)
        addx = playerx - Runtime.Runtime.SCREEN_X / 2
        addy = playery - Runtime.Runtime.SCREEN_Y / 2
        self.x = self.x + self.movex
        self.y = self.y + self.movey
        edge_multiplier = 1
        if self.x < -Runtime.Runtime.SCREEN_X*edge_multiplier or self.x > Runtime.Runtime.SCREEN_X*edge_multiplier:
            self.movex = self.movex * -1
            self.x = self.x + self.movex*2
        if self.y < -Runtime.Runtime.SCREEN_Y*edge_multiplier or self.y > Runtime.Runtime.SCREEN_Y*edge_multiplier:
            self.movey = self.movey * -1
            self.y = self.y + self.movey*2

        self.set_points()

        for x, y in zip(self.points[::2], self.points[1::2]):
            xx = x - playerx
            yy = y - playery
            self.coords[i] = xx * math.cos(r) + yy * math.sin(r) + playerx - addx
            self.coords[i + 1] = -xx * math.sin(r) + yy * math.cos(r) + playery - addy

            i = i + 2

        canvas.coords(self.img, self.coords)
        return True
