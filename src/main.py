"""
    Main module for running pg
"""

import pygame as pg
from enemy import Enemy
from hero import Hero
from constants import WIDTH, HEIGHT, TILESIZE, TITLE, BG_COLOUR, DARK_LINE

class Game:
    """
    Setup and run game instance
    """

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)

    def run(self):
        ''' Game loop '''

        self.playing = True
        while self.playing:
            self.events()
            self.draw()

    def new(self):
        ''' Creates sprites '''

        self.all_sprites = pg.sprite.Group()
        self.all_sprites.add(Enemy(1, 1))
        self.hero  = Hero()
        self.all_sprites.add(self.hero)
        # self.clock = pg.time.Clock()

    def draw_grid(self):
        ''' Draws the grid '''

        for x_pos in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, DARK_LINE, (x_pos, 0), (x_pos, HEIGHT))
        for y_pos in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, DARK_LINE, (0, y_pos), (WIDTH, y_pos))

    def draw(self):
        ''' Refreshes screen on every loop '''

        self.hero.handle_keys()
        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        pg.display.flip()
        # self.clock.tick(60)

    def events(self):
        ''' Event listener '''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False


# create instance of game
GAME = Game()
GAME.new()
GAME.run()
