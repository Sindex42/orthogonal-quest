''' Collision module '''

import os
import pygame as pg

def collide(subject, sprites, d_x=0, d_y=0, callback=None):
    ''' Check for collision '''

    for sprite in sprites:
        if sprite.x_pos == subject.x_pos + d_x and sprite.y_pos == subject.y_pos + d_y:
            if callback is not None:
                callback()
            return True
    return False

def bump_sound():
    ''' Generate bump sounds '''

    sound_bump = pg.mixer.Sound(os.path.join(
        'audio', 'sound_1.ogg'))
    chn_1 = pg.mixer.Channel(0)
    chn_1.set_volume(0.5)
    chn_1.play(sound_bump, 0)

def sound_effect(chn, vol):
    ''' Generates sound effects '''

    sound = pg.mixer.Sound(os.path.join(
        'audio', f'sound_{chn}.ogg'))
    channel = pg.mixer.Channel(chn)
    channel.set_volume(vol)
    channel.play(sound, 0)
