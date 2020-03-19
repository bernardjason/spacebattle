from Runtime import Runtime
from PlayerShip import PlayerShip
from Asteroid import Asteroid
from Stars import Stars

runtime = Runtime()
runtime.master.title("Hello World")
runtime.master.geometry("{}x{}".format(Runtime.SCREEN_X, Runtime.SCREEN_Y))

player = PlayerShip(runtime.main_canvas, 512, 400, runtime)
runtime.player = player
for xx in range(int(-Runtime.SCREEN_X ), int(Runtime.SCREEN_X*1.5), int(Runtime.SCREEN_X / 2)):
    for yy in range(int(-Runtime.SCREEN_Y ), int(Runtime.SCREEN_Y*1.5), int(Runtime.SCREEN_Y / 2)):
        asteroid = Asteroid(runtime.main_canvas, xx, yy)
        runtime.render_list.append(asteroid)

runtime.render_list.append(player)

for xx in range(int(-Runtime.SCREEN_X / 2), int(Runtime.SCREEN_X), int(Runtime.SCREEN_X / 2)):
    for yy in range(int(-Runtime.SCREEN_Y / 2), int(Runtime.SCREEN_Y), int(Runtime.SCREEN_Y / 2)):
        print(xx,yy)
        star = Stars(runtime.main_canvas, xx, yy)
        runtime.render_list.append(star)
        runtime.stars.append(star)
#star = Stars(runtime.main_canvas, Runtime.SCREEN_X*0.25, Runtime.SCREEN_Y*0.25)
#runtime.render_list.append(star)

runtime.mainloop()
