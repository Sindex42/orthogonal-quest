''' Hero module '''

import os
import pygame as pg


from constants import TILESIZE, BLACK


class Hero(pg.sprite.Sprite):
    ''' Create hero '''

    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        pg.mixer.init()
        self.game = game
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.orthogonal_boy_animation_setup()
        string = './images/orthogonal_boy/orthogonal_boy_down/orthogonal_boy_f0.png'
        self.image = pg.transform.scale(pg.image.load(
            string), (TILESIZE - 1, TILESIZE - 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.right_index = self.left_index = self.up_index = self.down_index = 0

    def move(self, d_x=0, d_y=0):
        ''' Defines hero movement '''

        if not self.collide_with_walls(
                d_x,
                d_y) and not self.collide_with_enemy(
                    d_x,
                    d_y):
            self.x_pos += d_x
            self.y_pos += d_y

        # Changes orthogonal_boy image on each arrow key push
        if d_x == 1:
            self.right_index += 1
            if self.right_index >= len(self.right_images):
                self.right_index = 0
            self.image = self.right_images[self.right_index].convert()
        if d_x == -1:
            self.left_index += 1
            if self.left_index >= len(self.left_images):
                self.left_index = 0
            self.image = self.left_images[self.left_index].convert()
        if d_y == 1:
            self.down_index += 1
            if self.down_index >= len(self.down_images):
                self.down_index = 0
            self.image = self.down_images[self.down_index].convert()
        if d_y == -1:
            self.up_index += 1
            if self.up_index >= len(self.up_images):
                self.up_index = 0
            self.image = self.up_images[self.up_index].convert()

    def collide_with_walls(self, d_x=0, d_y=0):
        ''' Check for wall collision '''

        for wall in self.game.walls_sprites:
            if wall.x_pos == self.x_pos + d_x and wall.y_pos == self.y_pos + d_y:
                print("Wall collision")
                sound_bump = pg.mixer.Sound(os.path.join(
                    'audio', 'Wall_Bump_Obstruction.ogg'))
                chn_1 = pg.mixer.Channel(0)
                chn_1.set_volume(0.5)
                chn_1.play(sound_bump, 0)
                return True
        return False

    def collide_with_enemy(self, d_x=0, d_y=0):
        ''' Check for enemy collision '''

        for enemy in self.game.enemy_sprites:
            if enemy.x_pos == self.x_pos + d_x and enemy.y_pos == self.y_pos + d_y:
                print("Game Over!")
                sound_game_over = pg.mixer.Sound(
                    os.path.join('audio', 'Game_Over.ogg'))
                chn_2 = pg.mixer.Channel(1)
                chn_2.set_volume(1.0)
                chn_2.play(sound_game_over, 0)
                self.kill()
                pg.time.delay(2200)
                self.game.playing = False
                return True
        return False

    def orthogonal_boy_animation_setup(self):
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

        for image in os.listdir('images/orthogonal_boy/orthogonal_boy_up'):
            path = os.path.join(
                'images/orthogonal_boy/orthogonal_boy_up', image)
            self.up_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_right_image(self):
        ''' Loads rightward facing sprites '''

        for image in os.listdir('images/orthogonal_boy/orthogonal_boy_right'):
            path = os.path.join(
                'images/orthogonal_boy/orthogonal_boy_right', image)
            self.right_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_down_image(self):
        ''' Loads downward facing sprites '''

        for image in os.listdir('images/orthogonal_boy/orthogonal_boy_down'):
            path = os.path.join(
                'images/orthogonal_boy/orthogonal_boy_down', image)
            self.down_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_left_image(self):
        ''' Loads leftward facing sprites '''

        for image in os.listdir('images/orthogonal_boy/orthogonal_boy_left'):
            path = os.path.join(
                'images/orthogonal_boy/orthogonal_boy_left', image)
            self.left_images.append(
                pg.transform.scale(
                    pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))

    def load_up_attack_image(self):
        ''' Load up facing sprite '''
        self.image = pg.transform.scale(
            pg.image.load(
                './images/orthogonal_boy/orthogonal_boy_attack/orthogonal_boy_ba.png'),
            (TILESIZE, TILESIZE)).convert()

    def load_down_attack_image(self):
        ''' Load down facing sprite '''

        self.image = pg.transform.scale(
            pg.image.load(
                './images/orthogonal_boy/orthogonal_boy_attack/orthogonal_boy_fa.png'),
            (TILESIZE, TILESIZE)).convert()

    def load_left_attack_image(self):
        ''' Load left facing sprite '''

        self.image = pg.transform.scale(
            pg.image.load(
                './images/orthogonal_boy/orthogonal_boy_attack/orthogonal_boy_la.png'),
            (TILESIZE, TILESIZE)).convert()

    def load_right_attack_image(self):
        ''' Load right facing sprite '''

        self.image = pg.transform.scale(
            pg.image.load(
                './images/orthogonal_boy/orthogonal_boy_attack/orthogonal_boy_ra.png'),
            (TILESIZE, TILESIZE)).convert()

    def update(self):
        ''' Update position '''

        self.rect.x = self.x_pos * TILESIZE + 1
        self.rect.y = self.y_pos * TILESIZE + 1
        self.image.set_colorkey(BLACK)
