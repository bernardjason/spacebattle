from tkinter import *
import Runtime
import math


class PlayerShip:
    pressedStatus = {"Left": False, "Right": False, "space": False, "Shift_L": False, "Up": False, "Down": False,
                     "Escape": False}

    def __init__(self, canvas: Canvas, x, y, runtime: Runtime):
        self.x = x
        self.y = y

        self.points = [self.x + 0, self.y + 0,
                       self.x + 50, self.y - 100,
                       self.x + 100, self.y + 0]
        self.coords = self.points.copy()
        self.img = canvas.create_polygon(self.points, outline="white", width=1)

        # self.player_gif = PhotoImage(file="player.gif")
        # self.img = canvas.create_image(x, y, image=self.player_gif)
        self.rotation = 0.0
        self.runtime = runtime
        for char in ["Left", "Right", "Up", "Down", "space", "Shift_L", "Escape"]:
            self.runtime.master.bind("<KeyPress-%s>" % char, PlayerShip.pressed)
            self.runtime.master.bind("<KeyRelease-%s>" % char, PlayerShip.released)

    def render(self, canvas: Canvas, dummy1, dummy2, dummy3):
        if PlayerShip.pressedStatus["Left"]:
            self.rotation = self.rotation - 0.5

        if PlayerShip.pressedStatus["Right"]:
            self.rotation = self.rotation + 0.5

        if PlayerShip.pressedStatus["Shift_L"]:
            r = math.radians(self.rotation - 90)
            self.x = self.x + 1 * math.cos(r)
            self.y = self.y + 1 * math.sin(r)

    def pressed(event):
        PlayerShip.pressedStatus[event.keysym] = True

    def released(event):
        PlayerShip.pressedStatus[event.keysym] = False
