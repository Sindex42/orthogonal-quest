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
        self.x = 0
        self.y = 0
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
 
 

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
        all_sprites.update()
    
        # Key line of code for rendering sprites
        all_sprites.draw(screen)
 
        pygame.display.flip()
 
        clock.tick(60)

        if event.type == pygame.QUIT:
            running = False
 
pygame.quit()