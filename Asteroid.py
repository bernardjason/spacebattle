from tkinter import *
import math
from Runtime import Runtime


class Asteroid:
    rotateAngle = 0.0

    def __init__(self, canvas: Canvas, x, y):
        self.x = x
        self.y = y
        self.centre_x = 50
        self.centre_y = 60
        self.points = [self.x + 0, self.y + 0,
                       self.x + 25, self.y + 60,
                       self.x + 50, self.y + 120,
                       self.x + 70, self.y + 70,
                       self.x + 100, self.y + 25,
                       self.x + 75, self.y + 0]
        self.coords = self.points.copy()
        self.img = canvas.create_polygon(self.points, outline="yellow", width=3)

    def render(self, canvas: Canvas,rotation,playerx,playery):
        i = 0
        r = math.radians(rotation)
        addx = playerx - Runtime.SCREEN_X/2
        addy = playery - Runtime.SCREEN_Y/2

        for x, y in zip(self.points[::2], self.points[1::2]):
            #xx = x - Runtime.SCREEN_X/2
            #yy = y - Runtime.SCREEN_Y/2
            #self.coords[i] = xx * math.cos(r) + yy * math.sin(r) + Runtime.SCREEN_X /2
            #self.coords[i + 1] = -xx * math.sin(r) + yy * math.cos(r) + Runtime.SCREEN_Y /2
            xx = x - playerx #- Runtime.SCREEN_X/2
            yy = y - playery # Runtime.SCREEN_Y/2
            self.coords[i] = xx * math.cos(r) + yy * math.sin(r) + playerx -addx#+Runtime.SCREEN_X/2
            self.coords[i + 1] = -xx * math.sin(r) + yy * math.cos(r) + playery-addy #+Runtime.SCREEN_Y/2
            #self.coords[i] =self.coords[i] + addx
            #self.coords[i + 1] = self.coords[i + 1] + addy

            i = i + 2

        canvas.coords(self.img, self.coords)
        self.rotateAngle = self.rotateAngle + 1
