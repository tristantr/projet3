"""
Module with all our game functionalities
"""

import pygame
from logic import constants


class Game:
    """
    Class to generate the game, that will be called in main

    """

    def __init__(self, element, element_graphic, isReplay):
        """
        Init method for the Game class

        Parameters
        ----------
        element : obj
            From Element class in Logic/element.py
        element_graphic: obj
            From ElementDisplay class in Graphic/element_graphic.py
        isReplay : bool
        """
        self.element = element
        self.element_graphic = element_graphic
        self.replay = False
        self.quit = False
        self.isReplayRun = isReplay

    def _event_quit_Pygame(self):
        """
        Quit pygame when you want by clicking the red cross

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def start_game(self):
        """
        Initialise pygame and start the game

        """
        pygame.init()
        pygame.display.set_caption("Projet3")
        self.font = pygame.font.SysFont('comicsans', 20, True)
        self._drawHomeScreenWindow()
        self._run_game()

    def _run_game(self):
        """
        Run the game after clicking the homescreen space bar

        """
        run = True
        while run:
            self._event_quit_Pygame()
            if [self.element.ennemy.x,
               self.element.ennemy.y] != [self.element.hero.get_x(),
                                          self.element.hero.get_y()]:
                self._move_character()
            else:
                run = False
        self._replay_or_quit()

    def _replay_or_quit(self):
        """
        Replay with new items position or quit pygame

        Returns
        -------
        self.replay: bool
            True if the player replays, wrong otherwise
        self.quit: bool
            True if the player quit, wrong otherwise

        """
        game_over = True
        while game_over:
            self._event_quit_Pygame()
            self._drawGameOverWindow()
            pygame.time.delay(10)
            keys = pygame.key.get_pressed()

            if keys[pygame.K_SPACE]:
                self.replay = True
                game_over = False
            elif keys[pygame.K_ESCAPE]:
                self.quit = True
                game_over = False

    def _move_character(self):
        """
        Replay with new items position or quit pygame

        """

        pygame.time.delay(100)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.element.hero.get_x() > constants.FIRST_PIXEL and [self.element.hero.get_x() - constants.SPRITE_SIZE, self.element.hero.get_y()] in self.element.stage.sprites_for_path:
            self.element.hero.go_left()

        if keys[pygame.K_RIGHT] and self.element.hero.get_x() < (constants.LAST_GAME_PIXEL - constants.SPRITE_SIZE) and [self.element.hero.get_x() + constants.SPRITE_SIZE, self.element.hero.get_y()] in self.element.stage.sprites_for_path:
            self.element.hero.go_right()

        if keys[pygame.K_UP] and self.element.hero.get_y() > constants.FIRST_PIXEL and [self.element.hero.get_x(), self.element.hero.get_y() - constants.SPRITE_SIZE] in self.element.stage.sprites_for_path:
            self.element.hero.go_up()

        if keys[pygame.K_DOWN] and self.element.hero.get_y() < (constants.LAST_GAME_PIXEL - constants.SPRITE_SIZE) and [self.element.hero.get_x(), self.element.hero.get_y() + constants.SPRITE_SIZE] in self.element.stage.sprites_for_path:
            self.element.hero.go_down()
        self._drawGameWindow()

# DRAW METHODS

    def _drawGameWindow(self):
        """
        Display the game window with up-to-date parameters

        """
        text = self.font.render('My inventory: ' + '{} / 4'.format(
            len(self.element_graphic.itemsDisplay.picked_items)),
            1, constants.WHITE)
        self.element_graphic.stageDisplay.display()
        self.element_graphic.stageDisplay.display_right_window()
        constants.SCREEN.blit(
            text,
            ((constants.LAST_GAME_PIXEL + constants.LAST_PIXEL) / 2 - text.get_width()/2,
             constants.SPRITE_SIZE))
        self.element_graphic.itemsDisplay.display()
        self.element_graphic.personnageDisplay.display()
        pygame.display.update()

    def _drawHomeScreenWindow(self):
        """
        Display the homescreen window

        """
        home_screen = True
        while home_screen and not self.isReplayRun:
            self._event_quit_Pygame()
            self.element_graphic.screenDisplay.displayHomeScreen()
            pygame.display.update()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                home_screen = False

    def _drawGameOverWindow(self):
        """
        Display the game-over window

        """
        self._event_quit_Pygame()
        if self.element_graphic.itemsDisplay.items_to_display != []:
            constants.SCREEN.blit(
                pygame.transform.scale(
                    pygame.image.load('Images/game_over.png'),
                    (constants.LAST_GAME_PIXEL // 2,
                     constants.LAST_GAME_PIXEL // 2)),
                (constants.LAST_GAME_PIXEL // 4,
                 constants.LAST_GAME_PIXEL // 4))
            self.element_graphic.personnageDisplay.remove_hero()
        else:
            constants.SCREEN.blit(
                pygame.transform.scale(
                    pygame.image.load('Images/you_win.png'),
                    (constants.LAST_GAME_PIXEL // 2,
                     constants.LAST_GAME_PIXEL // 2)),
                (constants.LAST_GAME_PIXEL // 4,
                 constants.LAST_GAME_PIXEL // 4))
        self.element_graphic.personnageDisplay.display()
        self.element_graphic.screenDisplay.displayPlayAgain()
        pygame.display.update()
