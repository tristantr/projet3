
import pygame
from logic import constants


class PersonnageDisplay:
    """
    Class to display our characters

    """
    def __init__(self, hero, ennemy):
        """
        Init method for the PersonnageDisplay class

        Parameters
        ----------
        hero : obj
            From Hero(Character) class in logic/characters.py

        ennemy : obj
            From Ennemy(Character) class in logic/characters.py    
        """           
        self.hero = hero
        self.ennemy = ennemy
        self.characters = [self.ennemy, self.hero]

    def display(self):
        """
        Display characters

        """   
        for character in self.characters:
            constants.SCREEN.blit(pygame.transform.scale(pygame.image.load(
                character.image), (constants.SPRITE_SIZE, constants.SPRITE_SIZE)), (character.x, character.y))

    def remove_hero(self):
        """
        Remove hero from the list of characters to display

        Returns
        -------
        list
            Characters to display, without the hero
        
        """          
        if len(self.characters) == 2:
            self.characters.pop(1)