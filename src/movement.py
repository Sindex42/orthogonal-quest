''' Hero movement module '''

import pygame as pg

def movement(event, hero):
    ''' Listens for all movement directions '''

    left(event, hero)
    right(event, hero)
    upwards(event, hero)
    downwards(event, hero)

def left(event, hero):
    ''' Triggers left movement '''

    if event.key == pg.K_a:
        hero.move(d_x=-1)
        hero.load_movement_image(0)

def right(event, hero):
    ''' Triggers right movement '''
    if event.key == pg.K_d:
        hero.move(d_x=1)
        hero.load_movement_image(4)

def upwards(event, hero):
    ''' Triggers up movement '''
    if event.key == pg.K_w:
        hero.move(d_y=-1)
        hero.load_movement_image(8)

def downwards(event, hero):
    ''' Triggers down movement '''

    if event.key == pg.K_s:
        hero.move(d_y=1)
        hero.load_movement_image(12)
