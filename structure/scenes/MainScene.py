#!/usr/bin/python3

from frame import Scene
from frame import Material
from frame import Color
from pygame.math import Vector2
from structure.game_objects.main_objects.Player import Player
from structure.game_objects.main_objects.EnemyGenerator import EnemyGenerator

from structure.game_objects.main_objects.BlackWrap import BlackWrap
from structure.game_objects.main_objects.LifeBar import LifeBar
from structure.game_objects.main_objects.MainController import MainController
from structure.game_objects.background_animator.ReverseStarCreator import ReverseStarCreator

player = Player(Vector2(300, 300))

main_scene = Scene([player, EnemyGenerator(), ReverseStarCreator(), LifeBar(Vector2(0, 0), player), MainController() , BlackWrap(Vector2(0, 0))], Material(Color.black))
