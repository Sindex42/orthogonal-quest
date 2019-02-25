''' Main module for running pg '''

from os import path
import pygame as pg
from hero import Hero
from enemy import Enemy
from wall import Wall
from constants import WIDTH, HEIGHT, TILESIZE, TITLE, BG_COLOUR, DARK_LINE, FONT_NAME, GREEN


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
        self.clock = pg.time.Clock()
        self.playing = None
        self.map_data = []
        self.load_data()
        self.counter = 0
        self.font_name = pg.font.match_font(FONT_NAME)

    def run(self):
        ''' Game loop '''

        self.playing = True
        while self.playing:
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
        #Currently draws text in game, this is for testing purposes
        self.draw_text_on_screen("Hello World!", 100, GREEN, 24, 24) 
        pg.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        self.screen.fill(BG_COLOUR)
        self.draw_text_on_screen(TITLE, 48, GREEN, WIDTH / 2, HEIGHT / 4)
        self.draw_text_on_screen("Arrows to move, Space bar to attack", 22, GREEN, WIDTH / 2, HEIGHT / 2)
        self.draw_text_on_screen("Press any key to play", 22, GREEN, WIDTH / 2, HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()
    
    def show_end_screen(self):
        # game splash/end screen
        pass
    
    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pg.event.get():
                if event == pg.QUIT:
                    waiting = False
                    self.playing = False
                if event == pg.KEYDOWN:
                    waiting = False

    def draw_text_on_screen(self, text, size, colour, x, y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, colour)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)


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
GAME.show_start_screen()
while GAME.playing:
    GAME.new()
    GAME.run()
pg.QUIT
