''' Sound module '''

import os
import pygame as pg

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
