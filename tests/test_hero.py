import pygame
import pytest
import sys
sys.path.append('../src')

from src.hero import Hero



class TestHero(object):
  def test_initial_x_position(self):
    hero = Hero()
    assert hero.x == 0

  def test_initial_y_position(self):
    hero = Hero()
    assert hero.y == 0



