import pygame

### LOGIQUE ###
SPRITE_SIZE = 40

hero_image = pygame.image.load('Images/MacGyver.png')

gardien_image = pygame.image.load('Images/gardien.png')


class Character:

	def __init__(self, x, y):
		self.x = x * 40
		self.y = y * 40	

class Hero(Character):

	def __init__(self, x, y):
		super().__init__(x, y)

	def go_up(self):
		self.y -= SPRITE_SIZE

	def go_down(self):
		self.y += SPRITE_SIZE

	def go_right(self):
		self.x += SPRITE_SIZE

	def go_left(self):
		self.x -= SPRITE_SIZE

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y			
	
class Ennemy(Character):

	def __init__(self, x, y):
		super().__init__(x, y)
		
	
	
			
