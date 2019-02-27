''' Runs the game '''

from game import Game
import pygame as pg
from info_screens import draw_text_on_screen, show_end_screen, show_start_screen


GAME = Game()
GAME.playing = True

while GAME.playing:
    show_start_screen(GAME)
    GAME.wait_for_key()
    GAME.new()
    GAME.run()
    show_end_screen(GAME)
    GAME.wait_for_key()
    
pg.quit()
