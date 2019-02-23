''' hero tiles '''

import pygame as pg
from constants import TILESIZE, BLACK


class hero(pg.sprite.Sprite):
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
    
    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy) and not self.collide_with_hero(dx, dy):
            self.x += dx
            self.y += dy
    
    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls_sprites:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                print("Wall collision")
                return True
        return False
    
    def collide_with_hero(self, d_x=0, d_y=0):
        ''' Check for hero collision '''
        for hero in self.game.all_sprites:
            if hero.x_pos == self.x_pos + d_x and hero.y_pos == self.y_pos + d_y:
                return True
        return False
