#!/usr/bin/python3


class Renderer:
    __game_display = 0

    @classmethod
    def set_display(cls, display):
        """
        This method sets the display for rendering
        :param display:
        """
        cls.__game_display = display

    @classmethod
    def render_background(cls, bg_material):
        """
        This method draws the background
        :param bg_material:
        """
        cls.__game_display.fill(bg_material.color)
