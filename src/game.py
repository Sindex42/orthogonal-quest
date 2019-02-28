''' Main module for game setup '''

from os import path
import pygame as pg
from hero import Hero
from enemy import Enemy
from boss import Boss
from wall import Wall
from hitbox import Hitbox
from collision import game_over_voice
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


class Game:
    ''' Setup and run game instance '''

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load('./audio/Bridgeburner (8-Bit).mp3')
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
        pg.display.set_caption(TITLE)

        self.walls_sprites = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.enemy_sprites = pg.sprite.Group()
        self.hero = None
        self.enemy = None
        self.win = None
        self.boss = None
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.playing = None
        self.map_data = []
        self.map_list = ['map1.txt', 'map2.txt', 'map3.txt', 'map4.txt']
        self.map_nr = 0
        self.counter = 0

    def run(self):
        ''' Game loop '''

        self.playing = True
        while self.playing:
            self.enemies_exist()
            self.move_enemies()
            self.events()
            self.update()
            self.draw()
            self.counter += 1

    def new(self):
        ''' Creates sprites '''
        self.load_data()

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.walls_sprites.add(Wall(self, col, row))
                if tile == 'E':
                    self.enemy_sprites.add(Enemy(self, col, row))
                if tile == 'H':
                    self.hero = Hero(self, col, row)
                    self.all_sprites.add(self.hero)

    def update(self):
        ''' Updates sprites '''

        self.all_sprites.update()
        self.enemy_sprites.update()

    def load_data(self):
        ''' Loads map '''

        self.map_data = []
        map_folder = path.join(path.dirname(__file__), 'maps')

        with open(path.join(map_folder, f'{self.map_list[self.map_nr]}'), 'r') as file:
            for line in file:
                self.map_data.append(line)

    def draw_grid(self):
        ''' Draws the grid '''

        for x_pos in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, GRID_COLOUR, (x_pos, 0), (x_pos, HEIGHT))
        for y_pos in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, GRID_COLOUR, (0, y_pos), (WIDTH, y_pos))

    def move_enemies(self):
        ''' Allows enemy to move '''

        for enemy in self.enemy_sprites:
            if self.counter > GAME_SPEED:
                enemy.move()
        if self.counter > GAME_SPEED:
            self.counter = 0

    def draw(self):
        ''' Refreshes screen on every loop '''

        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.walls_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        draw_hero_health(self.screen, 10, 10, self.hero.health / HERO_HEALTH)
        pg.display.flip()

     def enemies_exist(self):
        ''' Ends game if all enemies dead '''
        
        if not self.enemy_sprites:
            self.playing = False
            self.win = True
            self.end_game()

    def end_game(self):
        ''' End game process '''

        print("Game Over!")
        game_over_voice()
        self.hero.kill()
        self.playing = False

    def events(self):
        ''' Event listener '''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False
                pg.quit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    self.hero.move(d_x=-1)
                if event.key == pg.K_d:
                    self.hero.move(d_x=1)
                if event.key == pg.K_w:
                    self.hero.move(d_y=-1)
                if event.key == pg.K_s:
                    self.hero.move(d_y=1)

                if event.key == pg.K_RIGHT:
                    self.attack_event('right', 1, 0)
                if event.key == pg.K_LEFT:
                    self.attack_event('left', -1, 0)
                if event.key == pg.K_UP:
                    self.attack_event('up', 0, -1)
                if event.key == pg.K_DOWN:
                    self.attack_event('down', 0, 1)

    def attack_event(self, direction, d_x, d_y):
        ''' Executes player attack '''

        self.hero.load_attack_image(direction)
        hitbox = Hitbox(self, self.hero.x_pos + d_x, self.hero.y_pos + d_y)
        hitbox.collide_with_enemy()

    def wait_for_key(self):
        ''' Allows user to start game and quit '''
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
                    pg.quit()
                if event.type == pg.KEYDOWN:
                    waiting = False
                    self.playing = True
                    self.win = False
