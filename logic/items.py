import random
from logic import constants


class Item:
	def __init__(self, image, stage):
		self.image = image
		self.stage = stage
		random_coordonates_for_path = random.choice([ele for ele in stage.sprites_for_path if ele != constants.first_sprite and ele != constants.last_sprite])
		self.x = random_coordonates_for_path[0]
		self.y = random_coordonates_for_path[1]	





