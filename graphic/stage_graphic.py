from logic import stage
from logic import constants

class StageDisplay:
	def __init__(self, stage):
		self.stage = stage
		
	def display(self, display):
		wall_image = pygame.image.load('Images/floor-tiles-20x20.png')
		for sprite_for_wall in self.stage.sprites_for_walls:
  			screen.blit(wall_image,(sprite_for_wall[0], sprite_for_wall[1]))
		for sprite_for_path in self.stage.sprites_for_path:
  			pygame.draw.rect(screen, (255, 255, 255), (sprite_for_path[0], sprite_for_path[1], constants.SPRITE_SIZE, constants.SPRITE_SIZE))