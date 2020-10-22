from logic import constants

class Character:

	def __init__(self, x, y, image):
		self.x = x * constants.SPRITE_SIZE
		self.y = y * constants.SPRITE_SIZE
		self.image = image	

class Hero(Character):

	def __init__(self, x, y, image):
		super().__init__(x, y, image)

	def go_up(self):
		self.y -= constants.SPRITE_SIZE

	def go_down(self):
		self.y += constants.SPRITE_SIZE

	def go_right(self):
		self.x += constants.SPRITE_SIZE

	def go_left(self):
		self.x -= constants.SPRITE_SIZE

	def get_x(self):
		return self.x

	def get_y(self):
		return self.y			
	
class Ennemy(Character):

	def __init__(self, x, y, image):
		super().__init__(x, y, image)



			
