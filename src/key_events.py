import pygame as pg
from hero import Hero
from boss import Boss
from wall import Wall
from hitbox import Hitbox
from collision import game_over_voice, sword_slash_sound
from hud import draw_hero_health
from constants import (
    WIDTH,
    HEIGHT,
    TILESIZE,
    TITLE,
    BG_COLOUR,
    GRID_COLOUR,
    GAME_SPEED,
    HERO_HEALTH)

class Key_Events:

    def __init__(self, game):
        self.game = game

    def listen(self, hero):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.game.playing = False
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    hero.move(d_x=-1)
                    hero.load_movement_image(0)
                if event.key == pg.K_d:
                    hero.move(d_x=1)
                    hero.load_movement_image(4)
                if event.key == pg.K_w:
                    hero.move(d_y=-1)
                    hero.load_movement_image(8)
                if event.key == pg.K_s:
                    hero.move(d_y=1)
                    hero.load_movement_image(12)
