#!/usr/bin/python3

import pygame


class SoundPlayer:

    @classmethod
    def play_music(cls, music, loops=0, start=0.0):
        """
        This method plays  given music sound
        :param start: starting point of the music
        :param loops: number of loops f the music
        :param music: the sound object to be played
        """

        pygame.mixer.music.load(music)
        pygame.mixer.music.play(loops=loops, start=start)

    @classmethod
    def fade_out(cls):
        """
        This method fades out the current music
        """

        pygame.mixer.music.fadeout(2000)
