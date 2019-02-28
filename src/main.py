''' Runs the game '''

from game import Game
from info_screens import show_end_screen, show_start_screen

GAME = Game()
GAME.playing = True

while GAME.playing:
    if  GAME.map_nr == 0:
        show_start_screen(GAME)
        GAME.wait_for_key()
    GAME.new()
    GAME.run()
    show_end_screen(GAME)
    GAME.wait_for_key()
