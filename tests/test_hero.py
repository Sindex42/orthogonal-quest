import pytest
from unittest.mock import Mock
from src.hero import Hero

from doubles import InstanceDouble, allow

class TestHero(object):


  #Testing hero movement
  def test_hero_starting_position(self):
    game = ''
    hero = Hero(game, 0, 0)
    assert(hero.x) == 0
    assert(hero.y) == 0
  
  def test_hero_movement(self):
    Game2 = InstanceDouble('src.fakegame.Game2')
    allow(Game2).walls_sprites 
    hero = Hero(Game2, 0, 0)
    hero.move(1, 0)
    # hero.collide_with_walls = False 
    assert(hero.x) == 1
    assert(hero.y) == 0

  

  
