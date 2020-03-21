from tkinter import *
import math
import Runtime
import math


class Torpedo:

    def __init__(self, canvas: Canvas, start_rotation, x, y, dirx, diry):
        self.ttl = 400
        self.x = x
        self.y = y
        self.speed = 4
        self.dirx = dirx * self.speed
        self.diry = diry * self.speed
        self.start_rotation = 0 # start_rotation
        self.radius = 3
        self.img = canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius, self.y + self.radius, fill="red")
        self.screenx = x - Runtime.Runtime.SCREEN_X / 2
        self.screeny = y - Runtime.Runtime.SCREEN_Y / 2

    def render(self, canvas: Canvas, rotation, playerx, playery):
        self.y = self.y + self.diry
        self.x = self.x + self.dirx

        diff = rotation - self.start_rotation

        r = math.radians(diff)
        addx = playerx - Runtime.Runtime.SCREEN_X / 2
        addy = playery - Runtime.Runtime.SCREEN_Y / 2

        xx = self.x - playerx
        yy = self.y - playery
        self.screenx = xx * math.cos(r) + yy * math.sin(r) + playerx - addx
        self.screeny = -xx * math.sin(r) + yy * math.cos(r) + playery - addy

        canvas.coords(self.img,self.screenx - self.radius, self.screeny - self.radius, self.screenx + self.radius, self.screeny + self.radius)

        self.ttl = self.ttl - 1
        if self.ttl < 0:
            return False

        return True
