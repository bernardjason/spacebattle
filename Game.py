from Runtime import Runtime
from PlayerShip import PlayerShip
from Asteroid import Asteroid

runtime = Runtime()
runtime.master.title("Hello World")
runtime.master.geometry("{}x{}".format(Runtime.SCREEN_X,Runtime.SCREEN_Y))

player = PlayerShip(runtime.main_canvas, 512, 400,runtime)
runtime.player = player
asteroid1 = Asteroid(runtime.main_canvas,300,300)
asteroid2 = Asteroid(runtime.main_canvas,900,500)
runtime.render_list.append(asteroid1)
runtime.render_list.append(asteroid2)
runtime.render_list.append(player)




runtime.mainloop()





