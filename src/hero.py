''' Hero module '''

import os
import pygame as pg


from constants import TILESIZE, BLACK, HERO_HEALTH, MOB_DAMAGE
from collision import collide, bump_sound


class Hero(pg.sprite.Sprite):
    ''' Create hero '''

    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        pg.mixer.init()
        self.game = game
        self.x_pos = x_pos
        self.y_pos = y_pos

        string = './images/orthogonal_boy/orthogonal_boy_down/orthogonal_boy_f0.png'
        self.image = pg.transform.scale(pg.image.load(
            string), (TILESIZE - 1, TILESIZE - 1)).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.right_index, self.left_index, self.up_index, self.down_index = 0, 0, 0, 0
        self.up_images, self.right_images, self.down_images, self.left_images = [], [], [], []

        self.health = HERO_HEALTH

        self.animation_setup()

    def move(self, d_x=0, d_y=0):
        ''' Defines hero movement '''

        if not collide(self, self.game.walls_sprites, d_x, d_y, bump_sound) and not collide(
                self, self.game.enemy_sprites, d_x, d_y, self.end_game):
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

    def end_game(self):
        ''' End game process '''

        print("Ran into enemy")
        print("Game Over!")
        sound_game_over = pg.mixer.Sound(
            os.path.join('audio', 'Game_Over.ogg'))
        chn_2 = pg.mixer.Channel(1)
        chn_2.set_volume(1.0)
        chn_2.play(sound_game_over, 0)
        self.kill()
        pg.time.delay(2200)
        self.game.playing = False

    def animation_setup(self):
        ''' Assigns directional images to appropriate lists '''

        load_direction_image('up', self.up_images)
        load_direction_image('right', self.right_images)
        load_direction_image('down', self.down_images)
        load_direction_image('left', self.left_images)

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



def load_direction_image(direction, image_list):
    ''' Loads sprites for specific directions '''

    for image in os.listdir(f'images/orthogonal_boy/orthogonal_boy_{direction}'):
        path = os.path.join(f'images/orthogonal_boy/orthogonal_boy_{direction}', image)
        image_list.append(
            pg.transform.scale(
                pg.image.load(path), (TILESIZE - 1, TILESIZE - 1)))
