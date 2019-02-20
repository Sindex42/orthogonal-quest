import pygame
import pytest

from pynput.keyboard import Key, Controller

from src.hero import Hero

class TestHero(object):

  #Testing initial position
  def test_rect_x_position(self):
    hero = Hero()
    assert hero.rect.x == 240

  def test_rect_y_position(self):
    hero = Hero()
    assert hero.rect.y == 176

  #Testing hero movement
  def test_rect_new_position(self):
    pygame.init()
    pygame.display.set_mode((1024, 768))
    keyboard = Controller()
    keyboard.press(Key.down)
    hero = Hero()
    hero.handle_keys()
    
    assert hero.rect.y == 367
