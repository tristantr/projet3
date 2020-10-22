import pygame

from logic import characters
from logic import stage
from logic import items 
from logic import element
from logic import constants

from graphic import characters_graphic
from graphic import stage_graphic
from graphic import items_graphic
from graphic import element_graphic
from graphic import game

## CHARACTERS
macGyver = characters.Hero(constants.FIRST_SPRITE[0],constants.FIRST_SPRITE[1], 'Images/MacGyver.png')		
gardien = characters.Ennemy(constants.LAST_SPRITE[0] // constants.SPRITE_SIZE, constants.LAST_SPRITE[1] // constants.SPRITE_SIZE, 'Images/gardien.png')

## STAGE	
labyrinth = stage.Stage('Map/map1.txt')	
	
## ITEMS	
ether = items.Item('Images/ether.png', labyrinth)
aiguille = items.Item('Images/aiguille.png', labyrinth)
seringue = items.Item('Images/seringue.png', labyrinth)
tube = items.Item('Images/tube_plastique.png', labyrinth)

## PACK OF ITEMS
level_1_items = items.Pack_of_items(ether, aiguille, seringue, tube)

## SUPERCLASSE LOGIC
element = element.Element(macGyver, gardien, labyrinth, level_1_items)

## INSTANCES GRAPHIQUES
personnageDisplay = characters_graphic.PersonnageDisplay(element.hero, element.ennemy)
stageDisplay = stage_graphic.StageDisplay(element.stage)
itemsDisplay = items_graphic.ItemsDisplay(element.hero, element.items.items_to_display)

## SUPERCLASSE GRAPHIC
element_graphic = element_graphic.ElementDisplay(personnageDisplay, stageDisplay, itemsDisplay)

## GAME
game = game.Game(element, element_graphic)


def main():
	game.start_game()
	run = True
	while run:
		pygame.time.delay(100) 
		game.run_game()	
		game.redrawGameWindow()
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				run = False		 
	pygame.quit() 

if __name__ =='__main__':
	main()	
 





