''' Enemy module '''

from random import sample
import pygame as pg
from constants import TILESIZE, BLACK


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

    def move(self):
        ''' Defines enemy movement '''

        movement = sample(["up", "down", "left", "right"], 1)
        d_x = 0
        d_y = 0

        if movement == ["up"]:
            d_y = -1
        elif movement == ["down"]:
            d_y = 1
        elif movement == ["left"]:
            d_x = -1
        else:
            d_x = 1

        if not self.collide_with_walls(d_x, d_y) and not self.collide_with_hero(d_x, d_y):
            self.x_pos += d_x
            self.y_pos += d_y

    def collide_with_walls(self, d_x=0, d_y=0):
        ''' Check for wall collision '''

        for wall in self.game.walls_sprites:
            if wall.x_pos == self.x_pos + d_x and wall.y_pos == self.y_pos + d_y:
                print("Wall collision")
                return True
        return False

    def collide_with_hero(self, d_x=0, d_y=0):
        ''' Check for hero collision '''

        for hero in self.game.all_sprites:
            if hero.x_pos == self.x_pos + d_x and hero.y_pos == self.y_pos + d_y:
                print("Collision with hero")
                self.kill()
                self.game.playing = False
                return True
        return False

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
