import pygame as pg

def movement(event, hero):
    left(event, hero)
    right(event, hero)
    up(event, hero)
    down(event, hero)

def left(event, hero):
    if event.key == pg.K_a:
        hero.move(d_x=-1)
        hero.load_movement_image(0)

def right(event, hero):
    if event.key == pg.K_d:
        hero.move(d_x=1)
        hero.load_movement_image(4)

def up(event, hero):
    if event.key == pg.K_w:
        hero.move(d_y=-1)
        hero.load_movement_image(8)

def down(event, hero):
    if event.key == pg.K_s:
        hero.move(d_y=1)
        hero.load_movement_image(12)
