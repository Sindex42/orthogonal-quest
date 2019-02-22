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
