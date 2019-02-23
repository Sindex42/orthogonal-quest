import pygame
import pytest

from src.hero import Hero

class TestHero(object):

  #Testing initial position
  def test_rect_x_position(self):
    hero = Hero()
    assert hero.rect.x == 240

  def test_rect_y_position(self):
    hero = Hero()
    assert hero.rect.y == 176
<<<<<<< HEAD
=======

  #Testing hero movement
  def test_rect_new_position(self):
    pygame.init()
    pygame.display.set_mode((1024, 768))
    keyboard = Controller()
    keyboard.press(Key.down)



    assert hero.rect.y == 367
<<<<<<< HEAD
>>>>>>> Enemy moves around fast
=======
>>>>>>> d5f05a3b1db8e569960b5096e197914e642a699a
