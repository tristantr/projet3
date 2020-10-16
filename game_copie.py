import pygame
import random

from logic import element

from logic import constants

#from graphic import stage_graphic
#from graphic import characters_display
#from graphic import items_display

from logic import stage
from logic import characters
from logic import items


## Classe PERSONNAGE DISPLAY ##

class PersonnageDisplay: 
	def __init__(self, hero, ennemy):
		self.hero = hero 
		self.ennemy = ennemy
		self.characters = [self.hero, self.ennemy]
		
	def display(self, display):
		if [self.ennemy.x, self.ennemy.y] != [self.hero.x, self.hero.y]:
			screen.blit(pygame.transform.scale(pygame.image.load('Images/gardien.png'), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)), (self.ennemy.x, self.ennemy.y))
			screen.blit(pygame.transform.scale(pygame.image.load('Images/MacGyver.png'), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)), (self.hero.x, self.hero.y))
		else: 
			if element.items != []:
				screen.blit(pygame.transform.scale(pygame.image.load('Images/gardien.png'), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)), (self.ennemy.x, self.ennemy.y))
				screen.blit(pygame.transform.scale(pygame.image.load('Images/game_over.png'), (300, 300)), (constants.last_pixel // 2 - 150, constants.last_pixel // 2 - 150))				
			else: 
				screen.blit(pygame.transform.scale(pygame.image.load('Images/you_win.png'), (300, 300)), (constants.last_pixel // 2 - 150, constants.last_pixel // 2 - 150))
				screen.blit(pygame.transform.scale(pygame.image.load('Images/MacGyver.png'), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)), (self.hero.x, self.hero.y))
		
## CLASSE ITEM DISPLAY ##

class ItemsDisplay:
	def __init__(self, hero, list_of_items):
		self.hero = hero
		self.list_of_items = list_of_items
		self.i = 0

	def display(self, display):
		for item in self.list_of_items:
			if [item.x, item.y] != [self.hero.x, self.hero.y]:
				screen.blit(pygame.transform.scale(pygame.image.load(str(item.image)), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)),(item.x, item.y))
			else:
				element.items.remove(item)
				self.i += 1
				print('{} / 4'.format(self.i))			


## CLASSE STAGE DISPLAY

class StageDisplay:
	def __init__(self, stage):
		self.stage = stage
		
	def display(self, display):
		wall_image = pygame.image.load('Images/floor-tiles-20x20.png')
		for sprite_for_wall in self.stage.sprites_for_walls:
  			screen.blit(wall_image,(sprite_for_wall[0], sprite_for_wall[1]))
		for sprite_for_path in self.stage.sprites_for_path:
  			pygame.draw.rect(screen, (255, 255, 255), (sprite_for_path[0], sprite_for_path[1], constants.SPRITE_SIZE, constants.SPRITE_SIZE))

## Classe Bouton ##

#class Button: 
#	def __init__(self, x, y, text = ''):
#		self.color = (255, 255, 255)
#		self.x = x
#		self.y = y
#		self.text = text

#	def display(self, display):
#		pygame.draw.rect(screen, self.color, (self.x, self.y, 100, 100))
#		if self.text != '':
#			font = pygame.font.SysFont('comicsans', 80)
#			text = font.render(self.text, 1, (0,0,0))
#			screen.blit(text, (self.x, self.x))
	

	

## Classe Game ##

class Game:
	def __init__(self, element):
		self.element = element

	def start_game(self):
		pygame.init()
		pygame.display.set_caption("Projet3")	

	def run_game(self):
		keys = pygame.key.get_pressed() 
		self.element.hero.x = global_game.element.hero.get_x()
		self.element.hero.y = global_game.element.hero.get_y()

		if keys[pygame.K_LEFT] and self.element.hero.x > constants.first_pixel and [self.element.hero.x - constants.SPRITE_SIZE, self.element.hero.y] in labyrinth.sprites_for_path: 
			self.element.hero.go_left()	

		if keys[pygame.K_RIGHT] and self.element.hero.x < (constants.last_pixel - constants.SPRITE_SIZE) and [self.element.hero.x + constants.SPRITE_SIZE, self.element.hero.y] in labyrinth.sprites_for_path:
			self.element.hero.go_right()

		if keys[pygame.K_UP] and self.element.hero.y > constants.first_pixel and [self.element.hero.x, self.element.hero.y - constants.SPRITE_SIZE] in labyrinth.sprites_for_path:
			self.element.hero.go_up()

		if keys[pygame.K_DOWN] and self.element.hero.y < (constants.last_pixel - constants.SPRITE_SIZE) and [self.element.hero.x, self.element.hero.y + constants.SPRITE_SIZE] in labyrinth.sprites_for_path:
			self.element.hero.go_down()



	def replay_or_quit(self):
		pass


	#def stop_game(self):
	#	screen.blit(pygame.transform.scale(pygame.image.load('Images/game_over.png'), (300, 300)), (250, 250))	

	def redrawGameWindow(self):	 
	    stageDisplay.display(screen)
	    personnageDisplay.display(screen)
	    itemsDisplay.display(screen)
	    pygame.display.update() 


screen = pygame.display.set_mode((800,600))	
#button = Button(100, 100, 'Click Me')
labyrinth = stage.Stage('Map/map1.txt')

macGyver = characters.Hero(constants.first_sprite[0],constants.first_sprite[1])
gardien = characters.Ennemy(constants.last_sprite[0] // constants.SPRITE_SIZE, constants.last_sprite[1] // constants.SPRITE_SIZE)

element = element.Element(macGyver, gardien, labyrinth)

global_game = Game(element)

global_game.element.stage.generate()

ether = items.Item('Images/ether.png', labyrinth)
aiguille = items.Item('Images/aiguille.png', labyrinth)
seringue = items.Item('Images/seringue.png', labyrinth)
tube = items.Item('Images/tube_plastique.png', labyrinth)


element.add_item(ether)
element.add_item(aiguille)
element.add_item(seringue)
element.add_item(tube)

stageDisplay = StageDisplay(labyrinth)
itemsDisplay = ItemsDisplay(macGyver, element.items)
personnageDisplay = PersonnageDisplay(macGyver, gardien)

global_game.start_game()

run = True 

while run:	
	pygame.time.delay(100) 
	for event in pygame.event.get(): 
		if event.type == pygame.QUIT: 
			run = False  
	global_game.run_game()
	global_game.redrawGameWindow()	
	
pygame.quit() 
    

