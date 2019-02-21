import pygame as pg

from src.constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pg.sprite.Sprite):
    def __init__(self, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = TILESIZE * x_pos
        self.rect.y = TILESIZE * y_pos

    def handle_keys(self):
        """ Handles Keys """
        self.key = pg.key.get_pressed()
        self.__move_up_or_down()
        self.__move_left_or_right()
        self.__contain_right()
        self.__contain_left()
        self.__contain_bottom()
        self.__contain_top()

    # private methods

    def __move_up_or_down(self):
        if self.key[pg.K_DOWN]: # down key
            self.rect.y += TILESIZE
        elif self.key[pg.K_UP]: # up key
            self.rect.y -= TILESIZE

    def __move_left_or_right(self):
        if self.key[pg.K_RIGHT]: # right key
            self.rect.x += TILESIZE
        elif self.key[pg.K_LEFT]: # left key
            self.rect.x -= TILESIZE

    def __contain_right(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def __contain_left(self):
        if self.rect.left < 0:
            self.rect.left = 0

    def __contain_bottom(self):
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def __contain_top(self):
        if self.rect.top < 0:
            self.rect.top = 0
