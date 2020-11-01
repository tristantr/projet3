"""
Module to display the stage
"""
import pygame
from logic import constants


class StageDisplay:
    """
    Class to display sprites in the stage

    """
    def __init__(self, stage):
        """
        Init method for the ElementDisplay class

        Parameters
        ----------
        stage : obj
            From Stage class in logic/stage.py

        """
        self.stage = stage
        self.first_pixel_right_window = 600

    def display(self):
        """
        Display sprites for wall and sprite for path

        """
        wall_image = pygame.image.load('Images/floor-tiles-20x20.png')
        for sprite_for_wall in self.stage.sprites_for_walls:
            constants.SCREEN.blit(
                wall_image, (sprite_for_wall[0], sprite_for_wall[1]))
        for sprite_for_path in self.stage.sprites_for_path:
            pygame.draw.rect(
                constants.SCREEN,
                constants.WHITE,
                (sprite_for_path[0], sprite_for_path[1],
                 constants.SPRITE_SIZE, constants.SPRITE_SIZE))

    def display_right_window(self):
        """
        Display the inventory window

        """
        pygame.draw.rect(
            constants.SCREEN,
            constants.BLACK,
            (self.first_pixel_right_window, 0, 200, 600))
