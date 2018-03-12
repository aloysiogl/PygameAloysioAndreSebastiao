#!/usr/bin/python3

import pygame


class EventHandler:
    quit = False

    @classmethod
    def handle_events(cls, events_list):
        """
        This method updates the events list
        :param events_list:
        """

        for event in events_list:
            current_event = event.type

            if current_event == pygame.QUIT:
                cls.__quit()

    @classmethod
    def __quit(cls):
        """
        Quitting the game
        """
        cls.quit = True
