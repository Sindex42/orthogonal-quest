"""
    Main module for running pg
"""

import pygame as pg
from enemy import *
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
            self.events()
            self.draw()

    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Enemy(1, 1))

    def draw_grid(self):
       for x in range(0, WIDTH, TILESIZE):
           pg.draw.line(self.screen, DARK_LINE, (x, 0), (x, HEIGHT))
       for y in range(0, HEIGHT, TILESIZE):
           pg.draw.line(self.screen, DARK_LINE, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BACKGROUND_COLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

# create instance of game
game = Game()
game.new()
game.run()
