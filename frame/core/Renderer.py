#!/usr/bin/python3

import pygame
from pygame import gfxdraw


class Renderer:
    __game_display = 0

    @classmethod
    def set_display(cls, display):
        """
        This method sets the display for rendering
        :param display: current game display
        """
        cls.__game_display = display

    @classmethod
    def render_background(cls, bg_material):
        """
        This method draws the background
        :param bg_material: the material to be rendered as background
        """
        cls.__game_display.fill(bg_material.color)

    @classmethod
    def render_simple_circle(cls, circle_mesh, transform, mode):
        """
        This method renders a single colored circle
        :param mode: distinguish between different types of render
        :param circle_mesh: the mesh containing radius
        :param transform: the transform relations
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
        :param mode: distinguish between different types of render
        :param polygon_mesh: the mesh containing points
        :param transform: the transform relations
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

    @classmethod
    def render_simple_font(cls, font_mesh, transform, alpha):
        """
        This method renders a single colored text
        :param alpha: the text alpha
        :param font_mesh: the mesh to be rendered
        :param transform: the transform relations of the text
        """

        # Creating font

        font = pygame.font.Font(font_mesh.font, transform.scale)

        # Displaying the font

        color_alpha = tuple([int(alpha/255*x) for x in font_mesh.material.color])

        text = font.render(font_mesh.text, True, color_alpha)
        text2 = text.convert_alpha()
        text2.set_alpha(10)
        cls.__game_display.blit(text2, (transform.position.x, transform.position.y))
