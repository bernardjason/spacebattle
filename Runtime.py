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
    stars = list()
    asteroids = list()
    torpedos = list()

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

        i = 0
        startx = int(round((self.player.x - self.SCREEN_X / 2 - self.SCREEN_X / 2) / self.SCREEN_X) * self.SCREEN_X)
        starty = int(round((self.player.y - self.SCREEN_Y / 2 - self.SCREEN_Y / 2) / self.SCREEN_Y) * self.SCREEN_Y)
        for xx in range(startx, int(startx + self.SCREEN_X + 1), int(Runtime.SCREEN_X / 2)):
            for yy in range(starty, int(starty + self.SCREEN_Y + 1), int(Runtime.SCREEN_Y / 2)):
                self.stars[i].move_stars(xx, yy)
                i = i + 1
        if i != 9:
            print(i)
            exit(0)

        hitlist = list()
        for r in self.render_list:
            delete_me = r.render(self.main_canvas, self.player.rotation, self.player.x, self.player.y)
            if not delete_me:
                hitlist.append(r)

        for a in self.asteroids:
            for pi in range(0, len(self.player.points), 2):
                inside = self.point_inside_polygon(self.player.points[pi], self.player.points[pi + 1], a.coords)
                if inside:
                    self.asteroids.remove(a)
                    hitlist.append(a)
                    break
            for t in self.torpedos:
                if t.ttl < 0:
                    self.torpedos.remove(t)
                inside = self.point_inside_polygon(t.screenx,t.screeny,a.coords)
                if inside:
                    self.asteroids.remove(a)
                    self.torpedos.remove(t)
                    hitlist.append(a)
                    hitlist.append(t)
                    break

        for a in hitlist:
            if self.render_list.count(a) > 0:
                self.render_list.remove(a)
            self.main_canvas.delete(a.img)

        self.tps = self.tps + 1
        since = (start_time - self.timeStarted) / 1000
        self.topLabelText.set("TPS= " + str(round(self.tps / since)))
        elapsedTime = self.unix_time_millis() - start_time
        sleep = int(1000 / Runtime.REFRESH_RATE - elapsedTime)

        self.master.after(sleep, self.render)

    # http://www.ariel.com.au/a/python-point-int-poly.html
    def point_inside_polygon(self, x, y, poly):
        n = len(poly)
        inside = False

        p1x = poly[0]
        p1y = poly[1]
        for i in range(0,n + 1,2):
            p2x = poly[i % n]
            p2y = poly[ (i % n) +1]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside
