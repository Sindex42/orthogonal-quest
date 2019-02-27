''' Runs the game '''

import pygame as pg
from game import Game
from info_screens import show_end_screen, show_start_screen


GAME = Game('map2.txt')
GAME.playing = True

while GAME.playing:
    show_start_screen(GAME)
    GAME.wait_for_key()
    GAME.new()
    GAME.run()
    show_end_screen(GAME)
    GAME.wait_for_key()

pg.quit()
