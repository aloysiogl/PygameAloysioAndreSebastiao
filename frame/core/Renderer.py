#!/usr/bin/python3

import pygame
from pygame import gfxdraw
from pygame.math import Vector2


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
    def render_simple_circle(cls, circle_mesh, transform, mode):
        """
        This method renders a single colored circle
        :param mode:
        :param circle_mesh:
        :param transform:
        """

        pygame.gfxdraw.aacircle(cls.__game_display, int(transform.position.x), int(transform.position.y),
                                int(circle_mesh.radius * transform.scale), circle_mesh.material.color)
        if mode == 'Filled':
            pygame.gfxdraw.filled_circle(cls.__game_display, int(transform.position.x), int(transform.position.y),
                                     int(circle_mesh.radius * transform.scale), circle_mesh.material.color)

    @classmethod
    def render_simple_polygon(cls, polygon_mesh, transform, mode):
        """
        This method renders a single colored circle
        :param mode:
        :param polygon_mesh:
        :param transform:
        """

        # Getting points list

        points_list = []

        for point in polygon_mesh.points:
            distance_from_origin_local = point - polygon_mesh.pivot

            scaled_distance = distance_from_origin_local * transform.scale

            rotated_distance = scaled_distance.rotate(transform.rotation)

            points_list.append(rotated_distance + transform.position)

        # Drawing polygon
        pygame.gfxdraw.aapolygon(cls.__game_display, points_list, polygon_mesh.material.color)
        if mode == 'Filled':
            pygame.gfxdraw.filled_polygon(cls.__game_display, points_list, polygon_mesh.material.color)
