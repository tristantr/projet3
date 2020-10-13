class Weapon:
	def __init__(self, image, x, y):
		self.image = pygame.transform.scale(pygame.image.load(image), (40,40)) 		
		self.x = x
		self.y = y


ether = Weapon('Images/ether.png', a[0], a[1])



