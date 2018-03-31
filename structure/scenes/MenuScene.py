#!/usr/bin/python3


from frame import *
from frame.core.Representations import Screen
from structure.game_objects.menu_objects.MenuText import MenuText
from structure.game_objects.menu_objects.MenuController import MenuController
from structure.game_objects.menu_objects.StartText import StartText


def get_menu_scene():
    """
    This method creates a menu scene
    :return: The menu scene
    """

    menu_text = MenuText(Vector2(Screen.width/2, Screen.height/8))
    start_text = StartText(Vector2(Screen.width/2, Screen.height/2))
    menu_controller = MenuController()

    return Scene([menu_text, start_text, menu_controller], Material(Color.black))
