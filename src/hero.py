import pygame

HEIGHT = 768
WIDTH = 1024
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Hero(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
 
    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 32 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.rect.y += dist # move down
        elif key[pygame.K_UP]: # up key
            self.rect.y -= dist # move up
        if key[pygame.K_RIGHT]: # right key
            self.rect.x += dist # move right
        elif key[pygame.K_LEFT]: # left key
            self.rect.x -= dist # move left


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Orthogonal Quest')

all_sprites = pygame.sprite.Group()

hero = Hero()  
all_sprites.add(hero)
      
clock = pygame.time.Clock()

running = True
while running:

    for event in pygame.event.get():
        
        #print(event)
        screen.fill(WHITE)
        hero.handle_keys()
        all_sprites.update()

        # Key line of code for rendering sprites
        all_sprites.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

        if event.type == pygame.QUIT:
            running = False
 
pygame.quit()