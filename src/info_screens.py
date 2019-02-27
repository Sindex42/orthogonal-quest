''' Start and end screens '''

import pygame as pg
from constants import BG_COLOUR, TITLE, WIDTH, HEIGHT, GOLD, FONT_NAME


def draw_text_on_screen(game, text, size, x_pos, y_pos):
    ''' Draws text on screen '''
    font = pg.font.Font(pg.font.match_font(FONT_NAME), size)
    text_surface = font.render(text, True, GOLD)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x_pos, y_pos)
    game.screen.blit(text_surface, text_rect)

def show_start_screen(game):
    ''' Shows the start screen '''

    game.screen.fill(BG_COLOUR)
    draw_text_on_screen(game, TITLE, 48, WIDTH / 2, HEIGHT / 4)
    draw_text_on_screen(
        game,
        "Use 'W/A/S/D' keys to move and arrow keys to attack in their direction",
        22,
        WIDTH / 2,
        HEIGHT / 2)
    draw_text_on_screen(
        game,
        "Press any key to play",
        22,
        WIDTH / 2,
        HEIGHT * 3 / 4)
    pg.display.flip()

def show_end_screen(game):
    ''' Shows the end screen '''

    game.enemy_sprites.empty()
    game.all_sprites.empty()
    game.walls_sprites.empty()
    game.screen.fill(BG_COLOUR)
    draw_text_on_screen(game, "GAME OVER", 40, WIDTH / 2, HEIGHT / 2)
    draw_text_on_screen(
        game,
        "Press any key to play again",
        22,
        WIDTH / 2,
        HEIGHT * 3 / 4)
    pg.display.flip()
