import pygame
pygame.init()

DISPLAY = pygame.display.set_mode((600,600))
# chaque sprite sera un carré de 40 pxl de côté. Il y aura 15 sprites car 15 * 40 = 600
pygame.display.set_caption("Projet3")
hero_image = pygame.image.load('Images/MacGyver.png')

gardien_image = pygame.image.load('Images/gardien.png')
#ether_image = pygame.image.load('Images/ether.png')
#seringue_image = pygame.image.load('Images/seringue.png')
#aiguille_image = pygame.image.load('Images/aiguille.png')

SPRITE_SIZE = 40

Coordonates =[]
        # Ordonnées en premier 
        # Abscisse ensuite, pour avoir les coordonnées ligne par ligne et non pas colonne par colonne   
        # Cela va renvoyer [[0,0], [40,0], ..., [560,560]
for j in range(0, 15):                      
    for i in range (0, 15):                 
        Coordonates.append([i * SPRITE_SIZE, j * SPRITE_SIZE]) 
      
### LOGIQUE ###      

class Stage:
    def __init__(self, file):
        self.file = file
        self.Sprite_Value_0 = []
        self.Sprite_Value_1 = []

    def generate(self):
        #Sprite_Value_0 = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 0
        #Sprite_Value_1 = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 1
        file = open(str(self.file))
        read_file = file.read()
        Map = read_file.split()
            
        for i in range(0,225):
        # Si la valeur dans Map vaut 0, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_0    
            if Map[i] == str(0):        
                self.Sprite_Value_0.append(Coordonates[i])  
            else:
        # Si la valeur dans Map vaut 1, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_1            
                self.Sprite_Value_1.append(Coordonates[i])            

    def get_arrays(self):            
        return self.Sprite_Value_0
        return self.Sprite_Value_1         
		

### LOGIQUE ###
class Character:

	def __init__(self, x, y):
		self.x = x * SPRITE_SIZE
		self.y = y * SPRITE_SIZE

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

### AFFICHAGE ###		

	def draw(self, DISPLAY):
		DISPLAY.blit(hero_image,(self.x, self.y))	

### LOGIQUE###
class Ennemy(Character):

	def __init__(self, x, y):
		super().__init__(x, y)

### AFFICHAGE ###		
	
	def draw(self, DISPLAY):
		DISPLAY.blit(gardien_image, (self.x, self.y))		
			



### AFFICHAGE ###

def redrawGameWindow():
    #DISPLAY.blit(bg, (0,0))
   
    MacGyver.draw(DISPLAY)

    Gardien.draw(DISPLAY)
    pygame.display.update() # Met à jour l'écran dans la boucle infinie



# MAIN LOOP

# On initialise la boucle infinie While qui va nous permettre d'exécuter notre programme
run = True 
Labyrinth = Stage('Map/map1.txt')
Labyrinth.generate()
MacGyver = Hero(0, 0)
Gardien = Ennemy(14, 14)


# Tant que le jeu tourne, que se passe-t-il? 
while run:	
	pygame.time.delay(100) # met un petit delay dans le jeu, ici de l'ordre de 100 miliseconds, soit 0.1 seconde
# La loop va se faire au travers d'une liste d'evenements liés au clavier ou à la souris.	
	for event in pygame.event.get(): 
# Vérifie si on clique sur la croix rouge en haut à gauche		
		if event.type == pygame.QUIT: 
# Termine la boucle du jeu			
			run = False  

# On affiche les rectangles dont on a stocké les coordonnées [x,y] dans le tableau associées à 0 puis dans celui associé à 1. 
	for sprite0 in Labyrinth.Sprite_Value_0:
   		pygame.draw.rect(DISPLAY, (255,255,255), (sprite0[0], sprite0[1], SPRITE_SIZE, SPRITE_SIZE))

	for sprite1 in Labyrinth.Sprite_Value_1:
   		pygame.draw.rect(DISPLAY, (0,50,50), (sprite1[0], sprite1[1], SPRITE_SIZE, SPRITE_SIZE))

# On appelle la méthode get_pressed() de Pygame 
# Cela nous donne un dictionnaire ou chaque touche à la valeur 0 ou 1. 1 si on appuie sur la touche, 0 sinon.

	keys = pygame.key.get_pressed() 
	
# Si on appuie sur la flèche de gauche 	
	if keys[pygame.K_LEFT] and MacGyver.x > 0: 
		MacGyver.go_left()	

	if keys[pygame.K_RIGHT] and MacGyver.x < (600 - SPRITE_SIZE):
		MacGyver.go_right()

	if keys[pygame.K_UP] and MacGyver.y > 0:
		MacGyver.go_up()

	if keys[pygame.K_DOWN] and MacGyver.y < (600 - SPRITE_SIZE):
		MacGyver.go_down()
		
	redrawGameWindow()	
	
 # Si on sort de la boucle, on execute la méthode quit() et on quitte le jeu
pygame.quit() 
    

