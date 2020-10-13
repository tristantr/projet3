import pygame

### j'ai importé pygame dans la partie logique. C'est peut etre pas ce qui est demandé. C'est juste pour resizer les images dès que je créé une instance

SPRITE_SIZE = 40

class Character:

	def __init__(self, image, x, y):
		self.image = pygame.transform.scale(pygame.image.load(image), (40,40))
		self.x = x * 40
		self.y = y * 40	

class Hero(Character):

	def __init__(self, image, x, y):
		super().__init__(image, x, y)

	def go_up(self):
		self.y -= SPRITE_SIZE

	def go_down(self):
		self.y += SPRITE_SIZE

	def go_right(self):
		self.x += SPRITE_SIZE

	def go_left(self):
		self.x -= SPRITE_SIZE

#	def dont_move(self):
#		pass	

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y			
	
class Ennemy(Character):

	def __init__(self, image, x, y):
		super().__init__(image, x, y)
		
	
	
			
