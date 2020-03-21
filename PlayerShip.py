from tkinter import *
import Runtime
import math
from Torpedo import Torpedo
import Sound
import sys

class PlayerShip:
    pressedStatus = {"Left": False, "Right": False, "space": False, "Shift_L": False, "Up": False, "Down": False,
                     "Escape": False}
    speed = 2
    DONT_REPEAT = 30
    dont_repeat = DONT_REPEAT
    can_player_be_hit = 0

    def __init__(self, canvas: Canvas, runtime: Runtime):
        self.runtime = runtime
        self.x = 0
        self.y = 0
        self.rotation = 0.0
        self.middlex = 50
        self.middley = 50

        self.reset()

        self.points = [self.x - self.middlex, self.y + self.middley,
                       self.x , self.y - self.middley,
                       self.x + self.middlex, self.y + self.middley]
        self.coords = self.points.copy()
        self.img = canvas.create_polygon(self.points, outline="white", width=1)

        for char in ["Left", "Right", "Up", "Down", "space", "Shift_L", "Escape"]:
            self.runtime.master.bind("<KeyPress-%s>" % char, PlayerShip.pressed)
            self.runtime.master.bind("<KeyRelease-%s>" % char, PlayerShip.released)

    def reset(self):
        self.rotation = 0.0
        self.x = self.runtime.SCREEN_X/2
        self.y = self.runtime.SCREEN_Y/2

    colour_list=['red','red','orange','orange','yellow','yellow']
    def render(self, canvas: Canvas, dummy1, dummy2, dummy3):
        self.can_player_be_hit = self.can_player_be_hit +1
        if ( self.can_player_be_hit >= 0):
            canvas.itemconfig(self.img, outline='white')
        else:
            canvas.itemconfig(self.img, outline=self.colour_list[self.runtime.click%len(self.colour_list)])

        if PlayerShip.pressedStatus["Escape"]:
            sys.exit(0)

        if PlayerShip.pressedStatus["Left"]:
            self.rotation = self.rotation - 0.5

        if PlayerShip.pressedStatus["Right"]:
            self.rotation = self.rotation + 0.5

        if PlayerShip.pressedStatus["Shift_L"]:
            r = math.radians(self.rotation - 90)
            self.x = self.x + self.speed * math.cos(r)
            self.y = self.y + self.speed * math.sin(r)

        if PlayerShip.pressedStatus["space"] and self.dont_repeat > 0:
            Sound.fire()
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
