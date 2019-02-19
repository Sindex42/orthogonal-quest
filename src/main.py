"""
    Main module for running pygame
"""

import pygame

HEIGHT = 600
WIDTH = 800
GREEN = (0, 255, 0)

pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

RUNNING = True
while RUNNING:

    for event in pygame.event.get():
        print(event)
        SCREEN.fill(GREEN)
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
