import pygame as pg

from constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pg.sprite.Sprite):
    def __init__(self, game, x_pos, y_pos):

        pg.sprite.Sprite.__init__(self)
        self.game = game
        #self.image = pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1))
        self.x = x_pos
        self.y = y_pos

        self.up_index = 0
        self.up_images = []
        self.load_up_image()
        self.right_index = 0
        self.right_images = []
        self.load_right_image()
        self.down_index = 0
        self.down_images = []
        self.load_down_image()
        self.left_index = 0
        self.left_images = []
        self.load_left_image()

        self.image = self.image = pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1))
        self.rect = self.image.get_rect()

    def move(self, dx=0, dy=0):
        if not self.collide_with_walls(dx, dy) and not self.collide_with_enemy(dx, dy):
            self.x += dx
            self.y += dy
        #Changes link image on each arrow key push
        if dx == 1:
            #self.image = pg.transform.scale(pg.image.load('./images/link_r0.png'), (TILESIZE -1, TILESIZE -1))
            self.right_index += 1
            if self.right_index >= len(self.right_images):
                self.right_index = 0
            self.image = self.right_images[self.right_index]
        if dx == -1:
            #self.image = pg.transform.scale(pg.image.load('./images/link_l0.png'), (TILESIZE -1, TILESIZE -1))
            self.left_index += 1
            if self.left_index >= len(self.left_images):
                self.left_index = 0
            self.image = self.left_images[self.left_index]
        if dy == 1:
            self.image = pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1))
            self.down_index += 1
            if self.down_index >= len(self.down_images):
                self.down_index = 0
            self.image = self.down_images[self.down_index]
        if dy == -1:
            #self.image = pg.transform.scale(pg.image.load('./images/link_b0.png'), (TILESIZE -1, TILESIZE -1))    
            self.up_index += 1
            if self.up_index >= len(self.up_images):
                self.up_index = 0
            self.image = self.up_images[self.up_index]


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

    def load_up_image(self):
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b0.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b1.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b2.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b3.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b4.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b5.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b6.png'), (TILESIZE -1, TILESIZE -1)))
        self.up_images.append(pg.transform.scale(pg.image.load('./images/link_b7.png'), (TILESIZE -1, TILESIZE -1)))

    
    def load_right_image(self):
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r0.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r1.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r2.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r3.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r4.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r5.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r6.png'), (TILESIZE -1, TILESIZE -1)))
        self.right_images.append(pg.transform.scale(pg.image.load('./images/link_r7.png'), (TILESIZE -1, TILESIZE -1)))

    def load_down_image(self):
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f0.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f1.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f2.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f3.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f4.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f5.png'), (TILESIZE -1, TILESIZE -1)))
        self.down_images.append(pg.transform.scale(pg.image.load('./images/link_f6.png'), (TILESIZE -1, TILESIZE -1)))

    def load_left_image(self):
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l0.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l1.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l2.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l3.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l4.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l5.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l6.png'), (TILESIZE -1, TILESIZE -1)))
        self.left_images.append(pg.transform.scale(pg.image.load('./images/link_l7.png'), (TILESIZE -1, TILESIZE -1)))


    def update(self):
        self.rect.x = self.x * TILESIZE + 1
        self.rect.y = self.y * TILESIZE + 1
