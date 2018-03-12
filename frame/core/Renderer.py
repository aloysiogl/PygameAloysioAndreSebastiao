#!/usr/bin/python3

import pygame


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

    @classmethod
    def render_simple_circle(cls, circle_mesh, transform):
        """
        This method renders a single colored circle
        :param circle_mesh:
        :param transform:
        """
        pygame.draw.circle(cls.__game_display, circle_mesh.material.color,
                           [int(transform.position.x), int(transform.position.y)],
                           int(circle_mesh.radius*transform.scale))
