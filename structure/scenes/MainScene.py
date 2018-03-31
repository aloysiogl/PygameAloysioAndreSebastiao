#!/usr/bin/python3

from frame import Scene
from frame import Material
from frame import Color
from pygame.math import Vector2
from structure.game_objects.Player import Player
from structure.game_objects.EnemyGenerator import EnemyGenerator

main_scene = Scene([Player(Vector2(300,300)), EnemyGenerator()], Material(Color.white))
