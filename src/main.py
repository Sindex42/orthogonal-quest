''' Main module for running pg '''

from os import path
import pygame as pg
from hero import Hero
from enemy import Enemy
from wall import Wall
from constants import (WIDTH, HEIGHT, TILESIZE, TITLE, BG_COLOUR, DARK_LINE,
                       FONT_NAME, GOLD, GAME_SPEED)
from hitbox import Hitbox


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
        self.font_name = pg.font.match_font(FONT_NAME)

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
        pg.display.flip()


    def show_start_screen(self):
        ''' Shows the start screen '''
        # game splash/start screen
        self.screen.fill(BG_COLOUR)
        self.draw_text_on_screen(TITLE, 48, WIDTH / 2, HEIGHT / 4)
        self.draw_text_on_screen(
            "Use 'w/a/s/d' keys to move and arrow keys to attack in their direction",
            22,
            WIDTH / 2,
            HEIGHT / 2)
        self.draw_text_on_screen(
            "Press any key to play",
            22,
            WIDTH / 2,
            HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def show_end_screen(self):
        ''' Shows the end screen '''
        # game splash/end screen
        self.enemy_sprites.empty()
        self.all_sprites.empty()
        self.walls_sprites.empty()
        self.screen.fill(BG_COLOUR)
        self.draw_text_on_screen("GAME OVER", 40, WIDTH / 2, HEIGHT / 2)
        self.draw_text_on_screen(
            "Press a key to play again",
            22,
            WIDTH / 2,
            HEIGHT * 3 / 4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        ''' Allows user to start game and quit '''
        waiting = True
        while waiting:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.playing = False
                    pg.quit()
                if event.type == pg.KEYUP:
                    waiting = False
                    self.playing = True

    def draw_text_on_screen(self, text, size, x_pos, y_pos):
        ''' Draws text on screen '''
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, GOLD)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x_pos, y_pos)
        self.screen.blit(text_surface, text_rect)

    def enemies_exist(self):
        ''' Ends game if all enemies dead '''
        if not self.enemy_sprites:
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
                    self.hero.load_right_attack_image()
                    hitbox = Hitbox(self, self.hero.x_pos + 1, self.hero.y_pos)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_LEFT:
                    self.hero.load_left_attack_image()
                    hitbox = Hitbox(self, self.hero.x_pos - 1, self.hero.y_pos)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_UP:
                    self.hero.load_up_attack_image()
                    hitbox = Hitbox(self, self.hero.x_pos, self.hero.y_pos - 1)
                    hitbox.collide_with_enemy()
                if event.key == pg.K_DOWN:
                    self.hero.load_down_attack_image()
                    hitbox = Hitbox(self, self.hero.x_pos, self.hero.y_pos + 1)
                    hitbox.collide_with_enemy()


# create instance of game
GAME = Game()
GAME.show_start_screen()
while GAME.playing:
    GAME.new()
    GAME.run()
    GAME.show_end_screen()
pg.quit()
