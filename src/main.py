"""
    Main module for running pg
"""

import pygame as pg

HEIGHT = 600
WIDTH = 800
GREEN = (0, 255, 0)

pg.init()
SCREEN = pg.display.set_mode((WIDTH, HEIGHT))

RUNNING = True
while RUNNING:

    for event in pg.event.get():
        print(event)
        SCREEN.fill(GREEN)
        if event.type == pg.QUIT:
            RUNNING = False

    pg.display.flip()
