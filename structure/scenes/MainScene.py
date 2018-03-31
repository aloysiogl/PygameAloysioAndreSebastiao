#!/usr/bin/python3

from frame import Scene
from frame import Material
from frame import Color
from pygame.math import Vector2
from structure.game_objects.Player import Player
from structure.game_objects.EnemyGenerator import EnemyGenerator

from structure.game_objects.BlackWrap import BlackWrap
from structure.game_objects.LifeBar import LifeBar
from structure.game_objects.PowerBar import PowerBar

player = Player(Vector2(300,300))

main_scene = Scene([player, EnemyGenerator(), LifeBar(Vector2(0, 0), player), PowerBar(Vector2(340, 0), player), BlackWrap(Vector2(0, 0)), BlackWrap(Vector2(340, 0))], Material(Color.white))
