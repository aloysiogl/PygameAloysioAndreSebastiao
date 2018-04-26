#!/usr/bin/python3

from frame import *
from assets import pygame_textinput
from frame.core.Renderer import Renderer

import pygame


class ScoreController(GameObject):

    def __init__(self):
        """
        Controller for the score menu
        """
        super().__init__(Transform(Vector2(0, 0)))

        self.scores = []

        self.max_scores = 6
        self.line_size = 30

        self.got_name = False

        self.text_input = pygame_textinput.TextInput(font_family=Font.space_font, font_size=20, text_color=Color.white)

    def start(self):
        """
        Score initial configurations
        """

        file = open('scores.txt')
        lines = file.readlines()
        for w in lines:
            lines[lines.index(w)] = w.split(' ')

        # Sorting high scores

        lines = sorted(lines, key=lambda x: x[1], reverse=True)

        self.scores = lines

        file.close()

    def update(self):
        events = pygame.event.get()
        if self.text_input.update(events) and not self.got_name:
            # Updating scores
            self.scores.append([self.text_input.get_text(), str(SceneManager.score)+'\n'])
            self.scores = sorted(self.scores, key=lambda x: int(x[1]), reverse=True)

            # Outputting scores to file
            file = open('scores.txt', 'w')

            lines = [" ".join(x) for x in self.scores]

            file.writelines(lines)

            file.close()

            self.got_name = True

        if self.got_name and EventHandler.key_space:
            pass

    def draw(self):
        for i in range(min(self.max_scores, len(self.scores))):
            TextMesh(self.scores[i][0], Font.space_font, Material(Color.white)).render(
                Transform(Vector2(Vector2(100, 200+50*i)), 0, 20))
            TextMesh(self.scores[i][1], Font.space_font, Material(Color.white)).render(
                Transform(Vector2(Vector2(500, 200 + 50 * i)), 0, 20))

        if not self.got_name:
            TextMesh('Type your name: ', Font.space_font, Material(Color.white)).render(
                Transform(Vector2(Vector2(100, 500)), 0, 20))
            Renderer.render_text_input(self.text_input, Vector2(350, 500))
        else:
            TextMesh('Great! Press space beyond...', Font.space_font, Material(Color.white)).render(
                Transform(Vector2(Vector2(100, 500)), 0, 20))
