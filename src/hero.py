import pygame

from constants import WIDTH, HEIGHT, TILESIZE, GREEN


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
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

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
