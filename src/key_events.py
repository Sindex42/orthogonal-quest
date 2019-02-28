import pygame as pg
from hero import Hero
from boss import Boss
from wall import Wall
from hitbox import Hitbox
from collision import game_over_voice, sword_slash_sound
from hud import draw_hero_health
from movement import movement
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
            self.quit(event)

            if event.type == pg.KEYDOWN:

                movement(event, hero)
                self.attack(event)

    def attack(self, event):
        self.attack_left(event)
        self.attack_right(event)
        self.attack_up(event)
        self.attack_down(event)

    def quit(self, event):
        if event.type == pg.QUIT:
            self.game.playing = False
            pg.quit()

    def attack_right(self, event):
        if event.key == pg.K_RIGHT:
            self.game.attack_event('right', 1, 0)

    def attack_left(self, event):
        if event.key == pg.K_LEFT:
            self.game.attack_event('left', -1, 0)

    def attack_up(self, event):
        if event.key == pg.K_UP:
            self.game.attack_event('up', 0, -1)

    def attack_down(self, event):
        if event.key == pg.K_DOWN:
            self.game.attack_event('down', 0, 1)
