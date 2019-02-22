import pygame as pg

from src.constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pg.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1))
        self.rect = self.image.get_rect()
        self.x = x_pos
        self.y = y_pos

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy) and not self.collide_with_enemy(dx, dy):
            self.x += dx
            self.y += dy
        #Changes link image on each arrow key push
        if dx == 1:
            self.image = pg.transform.scale(pg.image.load('./images/link_r0.png'), (TILESIZE -1, TILESIZE -1))
        if dx == -1:
            self.image = pg.transform.scale(pg.image.load('./images/link_l0.png'), (TILESIZE -1, TILESIZE -1))
        if dy == 1:
            self.image = pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1))
        if dy == -1:
            self.image = pg.transform.scale(pg.image.load('./images/link_b0.png'), (TILESIZE -1, TILESIZE -1))    
    

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls_sprites:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                print("Wall collision")
                return True
        return False

    def collide_with_enemy(self, dx=0, dy=0):
        for enemy in self.game.all_sprites:
            if enemy.x == self.x + dx and enemy.y == self.y + dy:
                print("Enemy collision")
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE + 1
        self.rect.y = self.y * TILESIZE + 1
