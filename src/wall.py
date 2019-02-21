''' Wall tiles '''

import pygame as pg
from constants import TILESIZE, BROWN


class Wall(pg.sprite.Sprite):
    ''' Creates walls '''

    def __init__(self, x_pos, y_pos):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = TILESIZE * x_pos
        self.rect.y = TILESIZE * y_pos
