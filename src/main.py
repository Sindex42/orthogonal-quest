''' Main module for running pg '''

from os import path
import pygame as pg
from hero import Hero
from enemy import Enemy
from wall import Wall
from hitbox import Hitbox
from constants import WIDTH, HEIGHT, TILESIZE, TITLE, BG_COLOUR, DARK_LINE


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

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.playing = None
        self.map_data = []
        self.load_data()
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

        game_folder = path.dirname(__file__)

        with open(path.join(game_folder, 'map.txt'), 'r') as file:
            for line in file:
                self.map_data.append(line)

    def draw_grid(self):
        ''' Draws the grid '''

        for x_pos in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, DARK_LINE, (x_pos, 0), (x_pos, HEIGHT))
        for y_pos in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, DARK_LINE, (0, y_pos), (WIDTH, y_pos))

    def move_enemies(self):
        ''' Allows enemy to move '''

        for enemy in self.enemy_sprites:
            if self.counter > 30:
                enemy.move()

        if self.counter > 30:
            self.counter = 0

    def draw(self):
        ''' Refreshes screen on every loop '''

        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.walls_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        pg.display.flip()

    def enemies_exist(self):
        ''' Ends game if all enemies dead '''
        if not self.enemy_sprites:
            self.playing = False

    def events(self):
        ''' Event listener '''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

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
                    self.hero.load_attack_image('right')
                    hitbox = Hitbox(self, self.hero.x_pos + 1, self.hero.y_pos)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_LEFT:
                    self.hero.load_attack_image('left')
                    hitbox = Hitbox(self, self.hero.x_pos - 1, self.hero.y_pos)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_UP:
                    self.hero.load_attack_image('up')
                    hitbox = Hitbox(self, self.hero.x_pos, self.hero.y_pos - 1)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_DOWN:
                    self.hero.load_attack_image('down')
                    hitbox = Hitbox(self, self.hero.x_pos, self.hero.y_pos + 1)
                    hitbox.collide_with_enemy()


# create instance of game
GAME = Game()
GAME.new()
GAME.run()
