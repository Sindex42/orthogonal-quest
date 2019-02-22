''' Hero module '''

import pygame as pg

from constants import TILESIZE


class Hero(pg.sprite.Sprite):
    ''' Create hero '''

    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(pg.image.load(
            './images/link_f0.png'), (TILESIZE - 1, TILESIZE - 1))
        self.rect = self.image.get_rect()
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, d_x=0, d_y=0):
        ''' Move hero '''

        if not self.collide_with_walls(d_x, d_y) and not self.collide_with_enemy(d_x, d_y):
            self.x_pos += d_x
            self.y_pos += d_y

        # Changes link image on each arrow key push
        if d_x == 1:
            self.image = pg.transform.scale(
                pg.image.load('./images/link_r0.png'), (TILESIZE - 1, TILESIZE - 1))
        if d_x == -1:
            self.image = pg.transform.scale(
                pg.image.load('./images/link_l0.png'), (TILESIZE - 1, TILESIZE - 1))
        if d_y == 1:
            self.image = pg.transform.scale(
                pg.image.load('./images/link_f0.png'), (TILESIZE - 1, TILESIZE - 1))
        if d_y == -1:
            self.image = pg.transform.scale(
                pg.image.load('./images/link_b0.png'), (TILESIZE - 1, TILESIZE - 1))

    def collide_with_walls(self, d_x=0, d_y=0):
        ''' Check for wall collision '''

        for wall in self.game.walls_sprites:
            if wall.x_pos == self.x_pos + d_x and wall.y_pos == self.y_pos + d_y:
                print("Wall collision")
                return True
        return False

    def collide_with_enemy(self, d_x=0, d_y=0):
        ''' Check for enemy collision '''
        for enemy in self.game.all_sprites:
            if enemy.x_pos == self.x + d_x and enemy.y_pos == self.y + d_y:
                print("Game Over!")
                self.kill()
                self.game.playing = False
                return True
        return False

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
