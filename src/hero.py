import pygame

from src.constants import WIDTH, HEIGHT, TILESIZE, GREEN

class Hero(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def handle_keys(self):
        """ Handles Keys """
        self.key = pygame.key.get_pressed()
        self.__move_up_or_down()
        self.__move_left_or_right()
        self.__contain_right()
        self.__contain_left()
        self.__contain_bottom()
        self.__contain_top()

    # private methods

    def __move_up_or_down(self):
        if self.key[pygame.K_DOWN]: # down key
            self.rect.y += TILESIZE
        elif self.key[pygame.K_UP]: # up key
            self.rect.y -= TILESIZE

    def __move_left_or_right(self):
        if self.key[pygame.K_RIGHT]: # right key
            self.rect.x += TILESIZE
        elif self.key[pygame.K_LEFT]: # left key
            self.rect.x -= TILESIZE

    def __contain_right(self):
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def __contain_left(self):
        if self.rect.left < 0:
            self.rect.left = 0

    def __contain_bottom(self):
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def __contain_top(self):
        if self.rect.top < 0:
            self.rect.top = 0
