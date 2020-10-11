SPRITE_SIZE = 40

# Création d'une liste qui va contenir toutes les coordonnées [x,y] des sprites sous forme de tableau
# x est le premier élement du tableau, y le second

Coordonates =[]
        # Ordonnées en premier 
        # Abscisse ensuite, pour avoir les coordonnées ligne par ligne et non pas colonne par colonne   
        # Cela va renvoyer [[0,0], [40,0], ..., [560,560]
for j in range(0, 15):                      
    for i in range (0, 15):                 
        Coordonates.append([i * SPRITE_SIZE, j * SPRITE_SIZE]) 