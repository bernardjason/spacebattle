import Sound
from tkinter import *

score = 0
lives = 3
game_over = False
start_again = 0
game_over_text = None
debug = False

def start_game(runtime):
    global score, lives, game_over,start_again
    score = 0
    lives = 3
    game_over = False
    start_again = 0
    runtime.player.reset()

    if debug:
        runtime.add_asteroid(runtime.SCREEN_X/2,runtime.SCREEN_Y-300,1)
        runtime.add_asteroid(runtime.SCREEN_X/2,runtime.SCREEN_Y+300,1)
        runtime.add_asteroid(runtime.SCREEN_X/2+300,runtime.SCREEN_Y,1)
        runtime.add_asteroid(runtime.SCREEN_X/2-300,runtime.SCREEN_Y,1)
    else:
        for xx in range(int(-runtime.SCREEN_X/8), int(runtime.SCREEN_X*1.25), int(runtime.SCREEN_X / 2.5)):
            for yy in range(int(-runtime.SCREEN_Y/8), int(runtime.SCREEN_Y*1.25), int(runtime.SCREEN_Y / 2.5)):
                if xx != runtime.player.x and yy != runtime.player.y:
                    runtime.add_asteroid(xx,yy,5)


def hit_asteroid():
    global score,game_over
    if not game_over:
        score = score + 1


def player_hit():
    global lives,game_over
    if not game_over:
        lives = lives - 1
        Sound.player_dead()


def handle_game_over(runtime,canvas: Canvas, screen_width, screen_height,asteroids_left):
    global lives, game_over, score,start_again,game_over_text
    if (lives <= 0 or asteroids_left == 0) and not game_over:
        game_over = True
        game_over_text = canvas.create_text(int(screen_width / 3), int(screen_height / 2), fill="cyan", font="Times 40 italic bold",
                           text="Game over... score " + str(score))

    if game_over:
        start_again = start_again +1

    if start_again == 200:
        canvas.delete(game_over_text)
        game_over_text = canvas.create_text(int(screen_width / 3), int(screen_height / 2), fill="cyan", font="Times 40 italic bold",
                                            text="Starting soon")
    if start_again > 300:
        canvas.delete(game_over_text)
        start_game(runtime)
