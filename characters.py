SPRITE_SIZE = 40

class Character:
	def __init__(self, x, y):
		self.x = x * SPRITE_SIZE
		self.y = y * SPRITE_SIZE
		self.hitbox = [self.x, self.y, self.x + SPRITE_SIZE, self.y + SPRITE_SIZE]

	class Hero(Character):
		def __init__(self, x, y):	
			Character.init(x,y)


# Modifications des coordonnées du perso 
		def go_up():
			self.y -= SPRITE_SIZE

		def go_down():
			self.y += SPRITE_SIZE

		def go_right():
			self.x += SPRITE_SIZE	

		def go_left():
			self.x -= SPRITE_SIZE			

	
	class Ennemy(Character):
		def __init__(self, x, y):
			Character.init(x,y)			
