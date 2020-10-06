import pygame
pygame.init()

fichier = open('Map/map1.txt')

DISPLAY = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tableau Test")
SPRITE_SIZE = 40

# Création d'une liste qui va contenir toutes les coordonnées [x,y] des sprites sous forme de tableau
# x est le premier élement du tableau, y le second

fichier_read = fichier.read()
Map = fichier_read.split()

Coordonates =[]			

# Ordonnées en premier	
# Abscisse ensuite, pour avoir les coordonnées ligne par ligne et non pas colonne par colonne	
# Cela va renvoyer [[0,0], [40,0], ..., [560,560]	
for j in range(0, 15):						
	for i in range (0, 15):					
		Coordonates.append([i * 40, j * 40]) 
	

# On créé un tableau avec les coordonnées des élements associés à la valeur 0
Sprite_Value_0 = []	
# On créé un tableau avec les coordonnées des élements associés à la valeur 1
Sprite_Value_1 = []	

for i in range(0,225):
# Si la valeur dans Map vaut 0, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_0	
	if Map[i] == str(0):		
		Sprite_Value_0.append(Coordonates[i])	
	else:
# Si la valeur dans Map vaut 1, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_1			
		Sprite_Value_1.append(Coordonates[i])	
		

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

# Commande pour remplir l'écran en noir    
    #DISPLAY.fill((0,0,0))  

# On affiche les rectangles dont on a stocké les coordonnées [x,y] dans le tableau associées à 0 puis dans celui associé à 1. 
    for sprite0 in Sprite_Value_0:
    	pygame.draw.rect(DISPLAY, (255,255,255), (sprite0[0], sprite0[1], SPRITE_SIZE, SPRITE_SIZE))
 
    for sprite1 in Sprite_Value_1:
   		pygame.draw.rect(DISPLAY, (255,0,0), (sprite1[0], sprite1[1], SPRITE_SIZE, SPRITE_SIZE)) 
	

    pygame.display.update() 
    
pygame.quit()