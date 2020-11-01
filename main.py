import pygame

from logic import characters
from logic import stage
from logic import items
from logic.element import Element
from logic import constants

from graphic import screen_graphic
from graphic import characters_graphic
from graphic import stage_graphic
from graphic import items_graphic
from graphic.element_graphic import ElementDisplay
from graphic.game import Game


def main(isReplay = False):
    """
    Main function of the game
    Create all objects of our game: 
        - The hero
        - The ennemy
        - The stage
        - Items one by one
        - The pack of items
        - Objects for the Element and Element_graphic classes
        - The Game(element, element_graphic) object    

    """

    # CHARACTERS
    macGyver = characters.Hero(
        constants.FIRST_SPRITE[0], constants.FIRST_SPRITE[1], 'Images/MacGyver.png')
    gardien = characters.Ennemy(constants.LAST_SPRITE[0] // constants.SPRITE_SIZE,
                                constants.LAST_SPRITE[1] // constants.SPRITE_SIZE, 'Images/gardien.png')

    # STAGE
    labyrinth = stage.Stage('Map/map2.txt')

    # ITEMS
    ether = items.Item('Images/ether.png', labyrinth)
    aiguille = items.Item('Images/aiguille.png', labyrinth)
    seringue = items.Item('Images/seringue.png', labyrinth)
    tube = items.Item('Images/tube_plastique.png', labyrinth)

    # PACK OF ITEMS
    level_1 = items.Pack_of_items(ether, aiguille, seringue, tube)

    # SUPERCLASSE LOGIC
    element = Element(macGyver, gardien, labyrinth, level_1)

    # INSTANCES GRAPHIQUES
    personnageDisplay = characters_graphic.PersonnageDisplay(
        element.hero, element.ennemy)
    stageDisplay = stage_graphic.StageDisplay(element.stage)
    itemsDisplay = items_graphic.ItemsDisplay(
        element.hero, element.items.items_to_display)
    screenDisplay = screen_graphic.ScreenDisplay()

    # SUPERCLASSE GRAPHIC

    element_graphic = ElementDisplay(
        screenDisplay, personnageDisplay, stageDisplay, itemsDisplay)

    # GAME
    game = Game(element, element_graphic, isReplay)

    game.start_game()
    if game.replay:
        main(True)
    if game.quit:
        pygame.quit()
      
if __name__ == '__main__':
    main()