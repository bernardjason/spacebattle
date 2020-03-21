from PlayerShip import PlayerShip
from Stars import Stars
from Radar import Radar
from GameInfo import *
from Runtime import Runtime

runtime = Runtime()
runtime.master.title("Hello World")
runtime.master.attributes("-fullscreen", True)
Runtime.SCREEN_X = runtime.master.winfo_screenwidth()
Runtime.SCREEN_Y = runtime.master.winfo_screenheight()
runtime.master.geometry("{}x{}".format(Runtime.SCREEN_X, Runtime.SCREEN_Y))

player = PlayerShip(runtime.main_canvas, runtime)
runtime.player = player



runtime.render_list.append(player)
radar = Radar(runtime.main_canvas,Runtime.SCREEN_X-200,10,200)
runtime.radar = radar
for xx in range(int(-Runtime.SCREEN_X / 2), int(Runtime.SCREEN_X), int(Runtime.SCREEN_X / 2)):
    for yy in range(int(-Runtime.SCREEN_Y / 2), int(Runtime.SCREEN_Y), int(Runtime.SCREEN_Y / 2)):
        star = Stars(runtime.main_canvas, xx, yy)
        runtime.render_list.append(star)
        runtime.stars.append(star)

start_game(runtime)
runtime.mainloop()
