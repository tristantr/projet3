import pygame
from logic import constants

class Game:
	def __init__(self, element, element_graphic):
		self.element = element
		self.element_graphic = element_graphic

	def start_game(self):
		pygame.init()
		pygame.display.set_caption("Projet3")
		self.font = pygame.font.SysFont('comicsans', 20, True)	

	#def draw_home_screen(self):
	#	text_home_screen = self.font.render('Click on the Space Bar to start', 1, constants.WHITE)
	#	constants.HOME_SCREEN.blit(text_home_screen, ((constants.LAST_GAME_PIXEL + constants.LAST_PIXEL) / 2 - text_home_screen.get_width()/2, 40))

	def run_game(self):
		keys = pygame.key.get_pressed() 
		if keys[pygame.K_LEFT] and self.element.hero.get_x() > constants.FIRST_PIXEL and [self.element.hero.get_x() - constants.SPRITE_SIZE, self.element.hero.get_y()] in self.element.stage.sprites_for_path: 
			self.element.hero.go_left()

		if keys[pygame.K_RIGHT] and self.element.hero.get_x() < (constants.LAST_GAME_PIXEL - constants.SPRITE_SIZE) and [self.element.hero.get_x() + constants.SPRITE_SIZE, self.element.hero.get_y()] in self.element.stage.sprites_for_path:
			self.element.hero.go_right()

		if keys[pygame.K_UP] and self.element.hero.get_y() > constants.FIRST_PIXEL and [self.element.hero.get_x(), self.element.hero.get_y() - constants.SPRITE_SIZE] in self.element.stage.sprites_for_path:
			self.element.hero.go_up()

		if keys[pygame.K_DOWN] and self.element.hero.get_y() < (constants.LAST_GAME_PIXEL - constants.SPRITE_SIZE) and [self.element.hero.get_x(), self.element.hero.get_y() + constants.SPRITE_SIZE] in self.element.stage.sprites_for_path:
			self.element.hero.go_down()	

	def stop_game(self):
		pass
				
	def redrawGameWindow(self):
		text = self.font.render('My inventory: ' + '{} / 4'.format(len(self.element_graphic.itemsDisplay.picked_items)), 1, constants.WHITE)
		self.element_graphic.stageDisplay.display(constants.SCREEN)
		self.element_graphic.stageDisplay.display_right_window(constants.SCREEN)
		constants.SCREEN.blit(text, ((constants.LAST_GAME_PIXEL + constants.LAST_PIXEL) / 2 - text.get_width()/2, 40))
		self.element_graphic.itemsDisplay.display(constants.SCREEN)
		self.element_graphic.personnageDisplay.display(constants.SCREEN)
					

		if [self.element.ennemy.x, self.element.ennemy.y] == [self.element.hero.get_x(), self.element.hero.get_y()]:
			if self.element_graphic.itemsDisplay.items_to_display != []:
				constants.SCREEN.blit(pygame.transform.scale(pygame.image.load('Images/game_over.png'), (constants.LAST_GAME_PIXEL // 2, constants.LAST_GAME_PIXEL // 2)), (constants.LAST_GAME_PIXEL // 4, constants.LAST_GAME_PIXEL // 4))
				#self.element_graphic.personnageDisplay.remove_hero()			
			else:
				constants.SCREEN.blit(pygame.transform.scale(pygame.image.load('Images/you_win.png'), (constants.LAST_GAME_PIXEL // 2, constants.LAST_GAME_PIXEL // 2)), (constants.LAST_GAME_PIXEL // 4, constants.LAST_GAME_PIXEL // 4))	
		
		pygame.display.update() 



