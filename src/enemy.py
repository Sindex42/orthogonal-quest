'''' Enemy module '''

from random import sample
import pygame as pg
from constants import TILESIZE, BLACK, MOB_DAMAGE
from collision import collide


class Enemy(pg.sprite.Sprite):
    ''' Creates enemies '''

    def __init__(self, game, x_pos, y_pos):
        pg.sprite.Sprite.__init__(self)
        #Hero.__init__(self)
        #super(Hero, self).__init__()
        self.game = game
        self.image = None
        self.load_direction_image('down')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect.x = TILESIZE * x_pos + 1
        self.rect.y = TILESIZE * y_pos + 1

    def move(self):
        ''' Defines enemy movement '''

        movement = sample(['up', 'down', 'left', 'right'], 1).pop()
        self.load_direction_image(movement)
        d_x, d_y = 0, 0

        if movement == 'up':
            d_y = -1
        elif movement == 'down':
            d_y = 1
        elif movement == 'left':
            d_x = -1
        else:
            d_x = 1

        if not collide(self, self.game.walls_sprites, d_x, d_y) and not collide(
                self, self.game.all_sprites, d_x, d_y, self.enemy_touches_hero):
            self.x_pos += d_x
            self.y_pos += d_y

        if collide(self, self.game.all_sprites, d_x, d_y):
            self.enemy_touches_hero()

    def load_direction_image(self, direction):
        ''' Load directional facing sprites '''

        self.image = pg.transform.scale(
            pg.image.load(f'./images/skeleton/skeleton_{direction}.png'),
            (TILESIZE, TILESIZE)).convert()

    def enemy_touches_hero(self):
        ''' Updates Hero Health '''

        print("Enemy hit hero")
        self.game.hero.health -= MOB_DAMAGE
        if self.game.hero.health <= 0:
            self.game.end_game()

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
        self.image.set_colorkey(BLACK)
