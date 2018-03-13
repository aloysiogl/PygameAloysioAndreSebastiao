#!/usr/bin/python3

import pygame


class Timer:

    clock = pygame.time.Clock()

    @classmethod
    def register_frame(cls):
        """
        This method registers a game frame
        """

        cls.clock.tick(120)

    @classmethod
    def get_dt(cls):
        """
        This method gives the duration of a frame
        :return:
        """

        if cls.clock.get_fps() > 0:
            return cls.clock.get_fps() ** -1

        else:
            return None

    @classmethod
    def get_current_time(cls):
        """
        Retunrs the current time in seconds
        :return:
        """

        return pygame.time.get_ticks()/1000
