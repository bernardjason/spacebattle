from tkinter import *
from time import time
import PlayerShip
from Asteroid import Asteroid
from Radar import Radar
import Sound
import GameInfo

class Runtime:
    fps_counter = 1
    fps = 1
    REFRESH_RATE = 60
    render_list = list()
    SCREEN_X = 1920
    SCREEN_Y = 1024
    player: PlayerShip
    radar: Radar
    stars = list()
    asteroids = list()
    torpedos = list()
    click = 0

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

    def asteroid_hit_logic(self, a: Asteroid):
        GameInfo.hit_asteroid()
        offx=int(a.centre_x*1.25)
        offy=int(a.centre_y*1.25)
        if a.size > 1:
            for xx in range(int(a.x) - offx, int(a.x) + offx, offx):
                for yy in range(int(a.y) - offy,int(a.y)+offy,offy):
                    self.add_asteroid(xx,yy, a.size / 2)

    def add_asteroid(self, x, y, size):
        child1 = Asteroid(self.main_canvas, x, y, int(size))
        self.asteroids.append(child1)
        self.render_list.append(child1)

    def remove_all_asteroids(self):
        for a in self.asteroids:
            if self.render_list.count(a) > 0:
                self.render_list.remove(a)
            self.main_canvas.delete(a.img)
        self.asteroids.clear()

    def render(self):
        start_time = self.unix_time_millis()
        asteroid_hit = False
        self.click = self.click + 1
        if self.click % self.fps == 0:
            self.radar.update(self.main_canvas,self.player.x,self.player.y,self.player.rotation,self.asteroids)

        i = 0
        startx = int(round((self.player.x - self.SCREEN_X / 2 - self.SCREEN_X / 2) / self.SCREEN_X) * self.SCREEN_X)
        starty = int(round((self.player.y - self.SCREEN_Y / 2 - self.SCREEN_Y / 2) / self.SCREEN_Y) * self.SCREEN_Y)
        for xx in range(startx, int(startx + self.SCREEN_X + 1), int(Runtime.SCREEN_X / 2)):
            for yy in range(starty, int(starty + self.SCREEN_Y + 1), int(Runtime.SCREEN_Y / 2)):
                self.stars[i].move_stars(xx, yy)
                i = i + 1

        hitlist = list()
        for r in self.render_list:
            delete_me = r.render(self.main_canvas, self.player.rotation, self.player.x, self.player.y,self.fps)
            if not delete_me:
                hitlist.append(r)

        for a in self.asteroids:
            if self.player.can_player_be_hit >= 0:
                for pi in range(0, len(self.player.points), 2):
                    inside = self.point_inside_polygon(self.player.points[pi], self.player.points[pi + 1], a.coords)
                    if inside:
                        GameInfo.player_hit()
                        self.player.can_player_be_hit = -300
                        self.asteroid_hit_logic(a)
                        asteroid_hit = True
                        self.asteroids.remove(a)
                        hitlist.append(a)
                        break
            for t in self.torpedos:
                if t.ttl < 0:
                    self.torpedos.remove(t)
                inside = self.point_inside_polygon(t.screenx, t.screeny, a.coords)
                if inside:
                    self.asteroid_hit_logic(a)
                    asteroid_hit = True
                    self.asteroids.remove(a)
                    self.torpedos.remove(t)
                    hitlist.append(a)
                    hitlist.append(t)
                    break

        for a in hitlist:
            if self.render_list.count(a) > 0:
                self.render_list.remove(a)
            self.main_canvas.delete(a.img)

        if asteroid_hit:
            Sound.explode()

        GameInfo.handle_game_over(self,self.main_canvas,Runtime.SCREEN_X,Runtime.SCREEN_Y,len(self.asteroids))

        self.fps_counter = self.fps_counter + 1
        since = (start_time - self.timeStarted) / 1000
        self.fps =round(self.fps_counter / since )
        show = "FPS={} SCORE={} LIVES={}".format(str(self.fps), GameInfo.score, GameInfo.lives)
        self.topLabelText.set(show)
        elapsedTime = self.unix_time_millis() - start_time
        sleep = int(1000 / Runtime.REFRESH_RATE - elapsedTime)

        self.master.after(sleep, self.render)

    # http://www.ariel.com.au/a/python-point-int-poly.html
    def point_inside_polygon(self, x, y, poly):
        n = len(poly)
        inside = False

        p1x = poly[0]
        p1y = poly[1]
        for i in range(0, n + 1, 2):
            p2x = poly[i % n]
            p2y = poly[(i % n) + 1]
            if y > min(p1y, p2y):
                if y <= max(p1y, p2y):
                    if x <= max(p1x, p2x):
                        if p1y != p2y:
                            xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= xinters:
                            inside = not inside
            p1x, p1y = p2x, p2y

        return inside
