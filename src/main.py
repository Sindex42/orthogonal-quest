"""
    Main module for running pg
"""

import pygame as pg
from constants import *

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
