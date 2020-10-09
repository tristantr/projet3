### LOGIQUE ###
SPRITE_SIZE = 40

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

	def print(self):
		print(self.x)			

### AFFICHAGE ###		

	#def draw(self, DISPLAY):
	#	DISPLAY.blit(hero_image,(self.x, self.y))	

### LOGIQUE###
class Ennemy(Character):

	def __init__(self, x, y):
		super().__init__(x, y)

### AFFICHAGE ###		
	
	#def draw(self, DISPLAY):
	#	DISPLAY.blit(gardien_image, (self.x, self.y))		
			
