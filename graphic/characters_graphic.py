import pygame
from logic import constants

class PersonnageDisplay: 
	def __init__(self, hero, ennemy):
		self.hero = hero
		self.ennemy = ennemy
		self.characters = [self.ennemy, self.hero]
		
	def display(self, display):
		for character in self.characters:
			constants.SCREEN.blit(pygame.transform.scale(pygame.image.load(character.image), (constants.SPRITE_SIZE,constants.SPRITE_SIZE)), (character.x, character.y))

	def remove_hero(self):
		self.characters.pop()



	#def remove_ennemy(self):
	#	self.characters.pop(0)
				
