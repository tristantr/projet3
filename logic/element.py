class Element:	# super classe qui contient les personnages et le stage
	def __init__(self, hero, ennemy, stage):
		self.hero = hero
		self.ennemy = ennemy
		self.stage = stage
		self.items = []

	def add_item(self, objet):
		self.items.append(objet)	