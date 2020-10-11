import pygame
from logic import stage
from logic import characters

pygame.init()

DISPLAY = pygame.display.set_mode((600,600))

pygame.display.set_caption("Projet3")
hero_image = pygame.image.load('Images/MacGyver.png')
gardien_image = pygame.image.load('Images/gardien.png')
wall_image = pygame.image.load('Images/ether.png')


SPRITE_SIZE = 40

class Element:
	def __init__(self, character, stage):
		self.character = character
		self.stage = stage

class GraphicInterface:
	def __init__(self, element):
		self.element = element

	def draw_hero(self, DISPLAY):
		DISPLAY.blit(hero_image,(x, y))	

	def draw_ennemy(self, DISPLAY):
		DISPLAY.blit(gardien_image, (Gardien.x, Gardien.y))	


def redrawGameWindow():   
    graphic_interface.draw_hero(DISPLAY)
    graphic_interface.draw_ennemy(DISPLAY)
    pygame.display.update() # Met à jour l'écran dans la boucle infinie

# On initialise la boucle infinie While qui va nous permettre d'exécuter notre programme

Labyrinth = stage.Stage('Map/map1.txt')
MacGyver = characters.Hero(0, 0)
Gardien = characters.Ennemy(14, 14)
element = Element(MacGyver, Labyrinth)
graphic_interface = GraphicInterface(element)

graphic_interface.element.stage.generate()




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
   		#pygame.draw.rect(DISPLAY, (255,255,255), (sprite0[0], sprite0[1], SPRITE_SIZE, SPRITE_SIZE))
   		DISPLAY.blit(wall_image,(sprite_for_wall[0], sprite_for_wall[1]))

	for sprite_for_path in Labyrinth.sprites_for_path:
   		pygame.draw.rect(DISPLAY, (255, 255, 255), (sprite_for_path[0], sprite_for_path[1], SPRITE_SIZE, SPRITE_SIZE))

# On appelle la méthode get_pressed() de Pygame 
# Cela nous donne un dictionnaire ou chaque touche à la valeur 0 ou 1. 1 si on appuie sur la touche, 0 sinon.

	keys = pygame.key.get_pressed() 
	x = graphic_interface.element.character.get_x()
	y = graphic_interface.element.character.get_y()

	if keys[pygame.K_LEFT] and x > 0 and [x - SPRITE_SIZE, y] in Labyrinth.sprites_for_path: 
		MacGyver.go_left()	

	if keys[pygame.K_RIGHT] and x < (600 - SPRITE_SIZE) and [x + SPRITE_SIZE, y] in Labyrinth.sprites_for_path:
		MacGyver.go_right()

	if keys[pygame.K_UP] and y > 0 and [x, y - SPRITE_SIZE] in Labyrinth.sprites_for_path:
		MacGyver.go_up()

	if keys[pygame.K_DOWN] and y < (600 - SPRITE_SIZE) and [x, y + SPRITE_SIZE] in Labyrinth.sprites_for_path:
		MacGyver.go_down()
		
	redrawGameWindow()	
	
pygame.quit() 
    

