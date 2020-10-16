from logic import items
from logic import constants

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