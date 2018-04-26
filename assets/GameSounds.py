#!/usr/bin/python3

import pygame


class Music:
    menu_scene = 'assets/menu_scene_music.mp3'
    main_scene = 'assets/main_scene_music.mp3'


class Sound:

    @classmethod
    def get_sound(cls, name):
        """
        Gets a specified sound
        :param name: the name of the sound
        :return: the sound object
        """

        if name == 'blaster':
            return pygame.mixer.Sound('assets/blaster.wav')

