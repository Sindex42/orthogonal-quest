''' KeyEvents module '''

import pygame as pg
# from hero import Hero
from movement import movement

class KeyEvents:
    ''' Create key events '''

    def __init__(self, game):

        self.game = game

    def listen(self, hero):
        ''' Listens for all key events '''

        for event in pg.event.get():
            self.quit(event)

            if event.type == pg.KEYDOWN:

                movement(event, hero)
                self.attack(event)

    def attack(self, event):
        ''' Listens for attack events '''

        self.attack_left(event)
        self.attack_right(event)
        self.attack_up(event)
        self.attack_down(event)

    def quit(self, event):
        ''' Listens for quit event '''

        if event.type == pg.QUIT:
            self.game.playing = False
            pg.quit()

    def attack_right(self, event):
        ''' Triggers right attack '''

        if event.key == pg.K_RIGHT:
            self.game.attack_event('right', 1, 0)

    def attack_left(self, event):
        ''' Triggers left attack '''
        if event.key == pg.K_LEFT:
            self.game.attack_event('left', -1, 0)

    def attack_up(self, event):
        ''' Triggers up attack '''
        if event.key == pg.K_UP:
            self.game.attack_event('up', 0, -1)

    def attack_down(self, event):
        ''' Triggers down attack '''

        if event.key == pg.K_DOWN:
            self.game.attack_event('down', 0, 1)
