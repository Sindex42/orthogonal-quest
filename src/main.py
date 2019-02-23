''' Main module for running pg '''

from os import path
import pygame as pg
from hero import Hero
from enemy import Enemy
from wall import Wall
from constants import WIDTH, HEIGHT, TILESIZE, TITLE, BG_COLOUR, DARK_LINE


class Game:
    ''' Setup and run game instance '''

    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.mixer.music.load('./audio/Bridgeburner (8-Bit).mp3')
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
            self.enemymove()
            self.events()
            self.update()
            self.draw()
            self.counter += 1

    def new(self):
        ''' Creates sprites '''

        self.all_sprites = pg.sprite.Group()
        self.enemy = Enemy(self, 1, 1)
        self.hero = Hero(self, 5, 5)
        self.walls_sprites = pg.sprite.Group()

        self.all_sprites.add(self.hero)
        self.enemy_sprites.add(self.enemy)

        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    self.walls_sprites.add(Wall(self, col, row))

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

    def enemymove(self):
        ''' Allows enemy to move '''

        if self.counter > 30:
            self.enemy.move()
            self.counter = 0

    def draw(self):
        ''' Refreshes screen on every loop '''

        self.screen.fill(BG_COLOUR)
        self.draw_grid()
        self.all_sprites.draw(self.screen)
        self.walls_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        pg.display.flip()

    def events(self):
        ''' Event listener '''

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.playing = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.hero.move(d_x=-1)
                if event.key == pg.K_RIGHT:
                    self.hero.move(d_x=1)
                if event.key == pg.K_UP:
                    self.hero.move(d_y=-1)
                if event.key == pg.K_DOWN:
                    self.hero.move(d_y=1)


# create instance of game
GAME = Game()
GAME.new()
GAME.run()
