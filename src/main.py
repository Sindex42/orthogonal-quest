"""
    Main module for running pg
"""

import pygame as pg
from constants import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            for event in pg.event.get():
                self.screen.fill(GREEN)
                if event.type == pg.QUIT:
                    self.playing = False

            pg.display.flip()

# create instance of game
game = Game()
game.run()
