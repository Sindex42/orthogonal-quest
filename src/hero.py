import pygame as pg

from src.constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pg.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos

    def move(self, dx=0, dy=0):
        self.x += dx
        self.y += dy

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

    # private methods

    # def __move_up_or_down(self):
    #     if self.key[pg.K_DOWN]: # down key
    #         self.rect.y += TILESIZE
    #     elif self.key[pg.K_UP]: # up key
    #         self.rect.y -= TILESIZE

    # def __move_left_or_right(self):
    #     if self.key[pg.K_RIGHT]: # right key
    #         self.rect.x += TILESIZE
    #     elif self.key[pg.K_LEFT]: # left key
    #         self.rect.x -= TILESIZE

    # def __contain_right(self):
    #     if self.rect.right > WIDTH:
    #         self.rect.right = WIDTH

    # def __contain_left(self):
    #     if self.rect.left < 0:
    #         self.rect.left = 0

    # def __contain_bottom(self):
    #     if self.rect.bottom > HEIGHT:
    #         self.rect.bottom = HEIGHT

    # def __contain_top(self):
    #     if self.rect.top < 0:
    #         self.rect.top = 0
