''' Enemy module '''

from random import sample
import os
import pygame as pg
from constants import TILESIZE, BLACK


class Enemy(pg.sprite.Sprite):
    ''' Creates enemies '''

    def __init__(self, game, x_pos, y_pos):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.enemy_animation_setup()
        self.image = pg.transform.scale(
            pg.image.load('./images/skeleton/skeleton_down/skeleton_f0.png'),
            (TILESIZE - 1,
             TILESIZE - 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.right_index = self.left_index = self.up_index = self.down_index = 0
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
            self.up_index += 1
            if self.up_index >= len(self.up_images):
                self.up_index = 0
            self.image = self.up_images[self.up_index]
        elif movement == ["down"]:
            d_y = 1
            self.down_index += 1
            if self.down_index >= len(self.down_images):
                self.down_index = 0
            self.image = self.down_images[self.down_index]
        elif movement == ["left"]:
            d_x = -1
            self.left_index += 1
            if self.left_index >= len(self.left_images):
                self.left_index = 0
            self.image = self.left_images[self.left_index]
        else:
            d_x = 1
            self.right_index += 1
            if self.right_index >= len(self.right_images):
                self.right_index = 0
            self.image = self.right_images[self.right_index]

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

    def enemy_animation_setup(self):
        ''' Loops through index arrays and correct sprite image load methods '''

        self.up_index = self.right_index = self.down_index = self.left_index = 0
        self.up_images = []
        self.load_up_image()
        self.right_images = []
        self.load_right_image()
        self.down_images = []
        self.load_down_image()
        self.left_images = []
        self.load_left_image()

    def load_up_image(self):
        ''' Loads upward facing sprites '''

        for image in os.listdir('images/skeleton/skeleton_up'):
            path = os.path.join('images/skeleton/skeleton_up', image)
            self.up_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_right_image(self):
        ''' Loads rightward facing sprites '''

        for image in os.listdir('images/skeleton/skeleton_right'):
            path = os.path.join('images/skeleton/skeleton_right', image)
            self.right_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_down_image(self):
        ''' Loads downward facing sprites '''

        for image in os.listdir('images/skeleton/skeleton_down'):
            path = os.path.join('images/skeleton/skeleton_down', image)
            self.down_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_left_image(self):
        ''' Loads leftward facing sprites '''

        for image in os.listdir('images/skeleton/skeleton_left'):
            path = os.path.join('images/skeleton/skeleton_left', image)
            self.left_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
