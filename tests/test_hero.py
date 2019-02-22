import pygame
import pytest

# from pynput.keyboard import Key, Controller
from doubles import InstanceDouble, allow
from src.hero import Hero


class TestHero(object):

 

  #Testing hero movement
  def test_rect_new_position(self):
    game = ''
    hero = Hero(game, 0, 0)
    assert(hero.x) == 0
    assert(hero.y) == 0

  

  
