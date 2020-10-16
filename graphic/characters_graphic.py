from logic import characters
from logic import constants

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
		