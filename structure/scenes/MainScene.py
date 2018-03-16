#!/usr/bin/python3

from frame import Scene
from frame import Material
from frame import Color
from pygame.math import Vector2
from ..game_objects.Test import Test
from ..game_objects.Test3 import Test3

main_scene = Scene([Test(Vector2(100,100)), Test3(Vector2(300,300))], Material(Color.white))
