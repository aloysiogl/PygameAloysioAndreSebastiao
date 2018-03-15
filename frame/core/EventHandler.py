#!/usr/bin/python3

import pygame


class EventHandler:
    quit = False
    key_up = False
    key_down = False
    key_left = False
    key_right = False
    key_space = False


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
            elif current_event == pygame.KEYDOWN:
                cls.__keydown(event)
            elif current_event == pygame.KEYUP:
                cls.__keyup(event)

    @classmethod
    def __keydown(cls, current_event):
        """
        Updates keys on keydown
        """

        if current_event.key == pygame.K_UP:
            cls.key_up = True
        if current_event.key == pygame.K_DOWN:
            cls.key_down = True
        if current_event.key == pygame.K_LEFT:
            cls.key_left = True
        if current_event.key == pygame.K_RIGHT:
            cls.key_right = True
        if current_event.key == pygame.K_SPACE:
            cls.key_space = True

    @classmethod
    def __keyup(cls, current_event):
        """
        Updates key on keyup
        """

        if current_event.key == pygame.K_UP:
            cls.key_up = False
        if current_event.key == pygame.K_DOWN:
            cls.key_down = False
        if current_event.key == pygame.K_LEFT:
            cls.key_left = False
        if current_event.key == pygame.K_RIGHT:
            cls.key_right = False
        if current_event.key == pygame.K_SPACE:
            cls.key_space = False

    @classmethod
    def __quit(cls):
        """
        Quitting the game
        """
        cls.quit = True
