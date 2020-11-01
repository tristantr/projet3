"""
Module to display Home Screen and Play Again windows
"""
from logic import constants
import pygame


class ScreenDisplay:
    """
    Class to display Home Screen and Play Again windowes

    """
    def __init__(self):
        """
        Init method for the ScreenDisplay class
        """
        pass

    def displayHomeScreen(self):
        """
        Display the home screen window
        """
        pygame.draw.rect(
            constants.SCREEN,
            constants.WHITE,
            (0, 0, 800, constants.LAST_GAME_PIXEL))
        font = pygame.font.SysFont('comicsans', 30, True)
        text = font.render(
            'Press Space Bar to start the game', 1, constants.BLACK)
        constants.SCREEN.blit(
            text,
            (800 / 2 - text.get_width()/2,
             constants.LAST_GAME_PIXEL / 2 - text.get_height()/2))

    def displayPlayAgain(self):
        """
        Display the Play Again window depending on the game result
        """
        self.font2 = pygame.font.SysFont('comicsans', 30, True)
        self.text2 = self.font2.render(
            'Press Space Bar to play again or Escape to quit',
            1,
            constants.WHITE)
        pygame.draw.rect(
            constants.SCREEN,
            constants.BLACK,
            (constants.LAST_GAME_PIXEL / 2 - self.text2.get_width()/2,
             500,
             self.text2.get_width(),
             self.text2.get_height()))

        constants.SCREEN.blit(
            self.text2,
            (constants.LAST_GAME_PIXEL / 2 - self.text2.get_width()/2,
             500))
