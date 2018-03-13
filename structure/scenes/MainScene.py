#!/usr/bin/python3

from frame import Scene
from frame import Material
from frame import Color
from ..game_objects.Test import Test

main_scene = Scene([Test()], Material(Color.white))
