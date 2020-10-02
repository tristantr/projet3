import pygame
pygame.init()

DISPLAY = pygame.display.set_mode((600,600))
# chaque sprite sera un carré de 40 pxl de côté. Il y aura 15 sprites car 15 * 40 = 600
pygame.display.set_caption("Projet3")
hero_image = pygame.image.load('Images/MacGyver.png')
bg = pygame.image.load('Images/bg.jpg')
gardien_image = pygame.image.load('Images/gardien.png')
ether_image = pygame.image.load('Images/ether.png')
seringue_image = pygame.image.load('Images/seringue.png')
aiguille_image = pygame.image.load('Images/aiguille.png')



class Hero:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self. width = width # hauteur et largeur du sprite
		self.height = height
		self.vel = 40	# le personnage se déplace de 40 pxl en 40 pxl
		self.hitbox = [self.x, self.y, self.x + self.width, self.y + self.height]

	def draw(self, DISPLAY):
		DISPLAY.blit(hero_image,(self.x, self.y))	
		

class Plateau: 

	X_PLATEAU = 0
	Y_PLATEAU = 0

	def __init__(self):
		pass

	def draw(self, DISPLAY):
		for i in range(0,5):
			pygame.draw.rect(DISPLAY, (80,80,80), (i * 40, (i+1) * 40, 40, 40)) # On dessine les Sprites
			pygame.draw.rect(DISPLAY, (0,0,0), (i * 40, (i+3) * 40, 40, 40))



class Ennemy:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = [self.x, self.y, self.x + self.width, self.y + self.height]

	def draw(self, DISPLAY):
			DISPLAY.blit(gardien_image, (self.x, self.y))



def redrawGameWindow():
    DISPLAY.blit(bg, (0,0))
    Plateau1.draw(DISPLAY)    
    MacGyver.draw(DISPLAY)
    Gardien.draw(DISPLAY)
    pygame.display.update() # Met à jour l'écran dans la boucle infinie



# MAIN LOOP

run = True # on initialise la boucle infinie While qui va nous permettre d'exécuter notre programme
MacGyver = Hero(0, 0, 40, 40)
Gardien = Ennemy(560, 560, 40, 40)
Plateau1 = Plateau()

while run:	# tant que le jeu tourne, que se passe-t-il? 
	pygame.time.delay(100) # met un petit delay dans le jeu, ici de l'ordre de 100 miliseconds, soit 0.1 seconde
	for event in pygame.event.get():  # la loop va se faire au travers d'une liste d'evenements liés au clavier ou à la souris.
		if event.type == pygame.QUIT: # vérifie si on clique sur la croix rouge en haut à gauche
			run = False  # termine la boucle du jeu

	keys = pygame.key.get_pressed() # On appelle la méthode get_pressed() de Pygame 
	# Cela nous donne un dictionnaire ou chaque touche à la valeur 0 ou 1. 1 si on appuie sur la touche, 0 sinon.
	
	if keys[pygame.K_LEFT] and MacGyver.x > 0: # Si on appuie sur la flèche de gauche 
		MacGyver.x -= MacGyver.vel	

	if keys[pygame.K_RIGHT] and MacGyver.x < (600 - MacGyver.vel):
		MacGyver.x += MacGyver.vel

	if keys[pygame.K_UP] and MacGyver.y > 0:
		MacGyver.y -= MacGyver.vel

	if keys[pygame.K_DOWN] and MacGyver.y < (600 - MacGyver.vel):
		MacGyver.y += MacGyver.vel

	#if MacGyver.hitbox[2] > Gardien.x: and MacGyver.y >= Gardien.hitbox[3]:
		
	
	DISPLAY.fill((0,0,0))
	redrawGameWindow()	


	# pygame.draw.rect(DISPLAY, (255,0,0), (MacGyver.x, MacGyver.y, MacGyver.width, MacGyver.height))  # méthode pour faire un rectangle (Display (pour l'ajouter à l'écran), couleur, (x, y, width, height))


	

pygame.quit()  # Si on sort de la boucle, cela va être executé et on va quitter le jeu 
    

