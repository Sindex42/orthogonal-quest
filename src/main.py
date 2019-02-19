import pygame

HEIGHT = 600
WIDTH = 800
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

running = True
while running:

    for event in pygame.event.get():
        print(event)
        screen.fill(GREEN)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()