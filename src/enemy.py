''' Enemy tiles '''

import pygame as pg
from constants import TILESIZE, RED
from random import sample


class Enemy(pg.sprite.Sprite):
    ''' Creates enemies '''

    def __init__(self, game, x_pos, y_pos):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(
            pg.image.load('./images/imp_f0.png'),
            (TILESIZE - 1,
             TILESIZE - 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.x = TILESIZE * x_pos + 1
        self.rect.y = TILESIZE * y_pos + 1


    def update(self):
        self.rect.x = self.x * TILESIZE + 1
        self.rect.y = self.y * TILESIZE + 1

    def move(self):

        movement = sample(["up", "down", "left", "right"], 1)

        if movement == ["up"]:
            self.y += -1
        elif movement == ["down"]:
            self.y += +1
        elif movement == ["left"]:
            self.x += -1
        else:
            self.x += 1
