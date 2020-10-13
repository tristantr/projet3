import pygame
from logic import stage
from logic import characters
from logic import element
#from logic import objects
import random

pygame.init()

DISPLAY = pygame.display.set_mode((600,600))
pygame.display.set_caption("Projet3")

wall_image = pygame.image.load('Images/floor-tiles-20x20.png')


SPRITE_SIZE = 40
first_sprite = [0, 0]
last_sprite = [560, 560]

class Objects:
	def __init__(self, image, x, y):
		self.image = pygame.transform.scale(pygame.image.load(image), (40,40)) 		
		self.x = x
		self.y = y

class GraphicInterface:
	def __init__(self, element):
		self.element = element

	def draw_character(self, DISPLAY):
		DISPLAY.blit(element.ennemy.image, (Gardien.x, Gardien.y))		
		DISPLAY.blit(element.hero.image, (MacGyver.x, MacGyver.y))


def redrawGameWindow():   
    graphic_interface.draw_character(DISPLAY)
    pygame.display.update() # Met à jour l'écran dans la boucle infinie


Labyrinth = stage.Stage('Map/map1.txt')
MacGyver = characters.Hero('Images/MacGyver.png', first_sprite[0],first_sprite[1])
Gardien = characters.Ennemy('Images/gardien.png', last_sprite[0] // SPRITE_SIZE, last_sprite[1] // SPRITE_SIZE)
element = element.Element(MacGyver, Gardien, Labyrinth)
graphic_interface = GraphicInterface(element)


graphic_interface.element.stage.generate()

## à améliorer ###
## tout ça je vais essayer de le faire un nouveau module, le module objects ##
a = random.choice([ele for ele in Labyrinth.sprites_for_path if ele != first_sprite and ele != last_sprite])
b = random.choice([ele for ele in Labyrinth.sprites_for_path if ele != first_sprite and ele != last_sprite])
c = random.choice([ele for ele in Labyrinth.sprites_for_path if ele != first_sprite and ele != last_sprite])
d = random.choice([ele for ele in Labyrinth.sprites_for_path if ele != first_sprite and ele != last_sprite])


ether = Objects('Images/ether.png', a[0], a[1])
aiguille = Objects('Images/aiguille.png', b[0], b[1])
seringue = Objects('Images/seringue.png', c[0], c[1])
tube = Objects('Images/tube_plastique.png', d[0], d[1])


weapons = [ether, aiguille, seringue, tube]

run = True 


while run:	
	pygame.time.delay(100) # met un petit delay dans le jeu, ici de l'ordre de 100 miliseconds, soit 0.1 seconde
# La loop va se faire au travers d'une liste d'evenements liés au clavier ou à la souris.	
	for event in pygame.event.get(): 
# Vérifie si on clique sur la croix rouge en haut à gauche		
		if event.type == pygame.QUIT: 
# Termine la boucle du jeu			
			run = False  	

# On affiche les rectangles dont on a stocké les coordonnées [x,y] dans le tableau associées à 0 puis dans celui associé à 1. 
	for sprite_for_wall in Labyrinth.sprites_for_walls:

   		DISPLAY.blit(wall_image,(sprite_for_wall[0], sprite_for_wall[1]))

	for sprite_for_path in Labyrinth.sprites_for_path:
   		pygame.draw.rect(DISPLAY, (255, 255, 255), (sprite_for_path[0], sprite_for_path[1], SPRITE_SIZE, SPRITE_SIZE))


	keys = pygame.key.get_pressed() 
	MacGyver.x = graphic_interface.element.hero.get_x()
	MacGyver.y = graphic_interface.element.hero.get_y()

	for weapon in weapons:
		if [weapon.x, weapon.y] != [MacGyver.x, MacGyver.y]:
			DISPLAY.blit(weapon.image,(weapon.x, weapon.y))
		else:
			weapons.remove(weapon)


	if keys[pygame.K_LEFT] and MacGyver.x > 0 and [MacGyver.x - SPRITE_SIZE, MacGyver.y] in Labyrinth.sprites_for_path: 
		MacGyver.go_left()	

	if keys[pygame.K_RIGHT] and MacGyver.x < (600 - SPRITE_SIZE) and [MacGyver.x + SPRITE_SIZE, MacGyver.y] in Labyrinth.sprites_for_path:
		MacGyver.go_right()

	if keys[pygame.K_UP] and MacGyver.y > 0 and [MacGyver.x, MacGyver.y - SPRITE_SIZE] in Labyrinth.sprites_for_path:
		MacGyver.go_up()

	if keys[pygame.K_DOWN] and MacGyver.y < (600 - SPRITE_SIZE) and [MacGyver.x, MacGyver.y + SPRITE_SIZE] in Labyrinth.sprites_for_path:
		MacGyver.go_down()
		
	redrawGameWindow()	
	
pygame.quit() 
    

