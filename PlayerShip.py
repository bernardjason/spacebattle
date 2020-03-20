from tkinter import *
import Runtime
import math
from Torpedo import Torpedo


class PlayerShip:
    pressedStatus = {"Left": False, "Right": False, "space": False, "Shift_L": False, "Up": False, "Down": False,
                     "Escape": False}
    speed = 2
    DONT_REPEAT = 60
    dont_repeat = DONT_REPEAT

    def __init__(self, canvas: Canvas, x, y, runtime: Runtime):
        self.x = x
        self.y = y
        self.middlex = 50
        self.middley = 50

        self.points = [self.x - self.middlex, self.y + self.middley,
                       self.x , self.y - self.middley,
                       self.x + self.middlex, self.y + self.middley]
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
            self.x = self.x + self.speed * math.cos(r)
            self.y = self.y + self.speed * math.sin(r)

        if PlayerShip.pressedStatus["space"] and self.dont_repeat > 0:
            self.dont_repeat = - self.DONT_REPEAT
            r = math.radians(self.rotation-90)
            dirx = math.cos(r)
            diry = math.sin(r)
            t = Torpedo(self.runtime.main_canvas,self.rotation-270,self.x,self.y,dirx,diry)
            self.runtime.render_list.append(t)
            self.runtime.torpedos.append(t)

        self.dont_repeat = self.dont_repeat + 1
        return True

    def pressed(event):
        PlayerShip.pressedStatus[event.keysym] = True

    def released(event):
        PlayerShip.pressedStatus[event.keysym] = False
