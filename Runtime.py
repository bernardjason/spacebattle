from tkinter import *
from time import time
import PlayerShip


class Runtime:
    tps = 0
    REFRESH_RATE = 60
    render_list = list()
    SCREEN_X = 1024
    SCREEN_Y = 800
    player: PlayerShip

    def __init__(self):
        self.master = Tk()
        self.text_canvas = Canvas(self.master, bg="green")
        self.text_canvas.pack(fill=X)
        self.topLabelText = StringVar()
        Label(self.text_canvas, textvariable=self.topLabelText, bg="green", fg="black").pack(side=LEFT)
        self.main_canvas = Canvas(self.master, bg="black")
        self.main_canvas.pack(fill=BOTH, expand=True)
        self.timeStarted = self.unix_time_millis()

    def mainloop(self):
        self.master.after(10, self.render)
        self.master.mainloop()

    @staticmethod
    def unix_time_millis():
        return int(time() * 1000)

    def render(self):
        start_time = self.unix_time_millis()

        for r in self.render_list:
            r.render(self.main_canvas, self.player.rotation,self.player.x,self.player.y)

        self.tps = self.tps + 1
        since = (start_time - self.timeStarted) / 1000
        self.topLabelText.set("Hello World " + str(self.tps / since))
        elapsedTime = self.unix_time_millis() - start_time
        sleep = int(1000 / Runtime.REFRESH_RATE - elapsedTime)

        self.master.after(sleep, self.render)
