''' HUD module '''

import pygame as pg
from constants import BAR_HEIGHT, BAR_LENGTH, WHITE, GREEN, YELLOW, RED 


def draw_hero_health(surf, x_pos, y_pos, pct):
    ''' Draws Hero Health Bar'''

    if pct < 0:
        pct = 0
    fill = pct * BAR_LENGTH
    outline_rect = pg.Rect(x_pos, y_pos, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pg.Rect(x_pos, y_pos, fill, BAR_HEIGHT)
    if pct > 0.6:
        col = GREEN
    elif pct > 0.3:
        col = YELLOW
    else:
        col = RED
    pg.draw.rect(surf, col, fill_rect)
    pg.draw.rect(surf, WHITE, outline_rect, 2)
