''' Hero module '''

import pygame as pg

from constants import TILESIZE, BLACK, HERO_HEALTH, MOB_DAMAGE
from collision import collide, bump_sound, enemy_impact_sound


class Hero(pg.sprite.Sprite):
    ''' Create hero '''

    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        pg.mixer.init()
        self.game = game
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = pg.transform.scale(pg.image.load(
            './images/hero/movement/hero_12.png'), (TILESIZE - 1, TILESIZE - 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.index_counter = -1
        self.health = HERO_HEALTH

    def move(self, d_x=0, d_y=0):
        ''' Defines hero movement '''

        if not collide(self, self.game.walls_sprites, d_x, d_y, bump_sound) and not collide(
                self, self.game.enemy_sprites, d_x, d_y, self.hero_touches_enemy):
            self.x_pos += d_x
            self.y_pos += d_y

    def load_movement_image(self, index):
        ''' Loads hero movements images '''

        self.index_counter += 1
        if self.index_counter >= 4:
            self.index_counter = 0
        i = self.index_counter + index
        self.image = pg.transform.scale(pg.image.load(
            f'./images/hero/movement/hero_{i}.png'), (TILESIZE - 1, TILESIZE - 1)).convert()

    def hero_touches_enemy(self):
        ''' Updates Hero Health '''

        print("Ran into enemy")
        enemy_impact_sound()
        self.health -= MOB_DAMAGE
        if self.health <= 0:
            self.game.end_game()

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
        self.image.set_colorkey(BLACK)

    def load_attack_image(self, direction):
        ''' Loads sprites for directional attacking '''

        self.image = pg.transform.scale(
            pg.image.load(
                f'./images/hero/hero_attack/hero_{direction}.png'),
            (TILESIZE, TILESIZE)).convert()
