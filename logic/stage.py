## CONSTANTE


SPRITE_SIZE = 40

# Création d'une liste qui va contenir toutes les coordonnées [x,y] des sprites sous forme de tableau
# x est le premier élement du tableau, y le second

#Coordonates =[]
        # Ordonnées en premier 
        # Abscisse ensuite, pour avoir les coordonnées ligne par ligne et non pas colonne par colonne   
        # Cela va renvoyer [[0,0], [40,0], ..., [560,560]
#for j in range(0, 15):                      
#    for i in range (0, 15):                 
#        Coordonates.append([i * SPRITE_SIZE, j * SPRITE_SIZE]) 
      
### LOGIQUE ###      

class Stage:
    def __init__(self, file):
        self.file = file
        self.sprite_value_0 = []
        self.sprite_value_1 = []
        self._create_coordonates()

    def _create_coordonates(self):
        self.coordonates = []
        for j in range(0, 15):                      
            for i in range (0, 15):                 
                self.coordonates.append([i * SPRITE_SIZE, j * SPRITE_SIZE]) 


    def generate(self):
        #Sprite_Value_0 = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 0
        #Sprite_Value_1 = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 1
        file = open(str(self.file))
        read_file = file.read()
        Map = read_file.split()
            
        for i in range(0,225):
        # Si la valeur dans Map vaut 0, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_0    
            if Map[i] == str(0):        
                self.sprite_value_0.append(self.coordonates[i])  
            else:
        # Si la valeur dans Map vaut 1, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprite_Value_1            
                self.sprite_value_1.append(self.coordonates[i])                   

    def get_arrays(self):            
        return self.sprite_value_0, self.sprite_value_1  # modifier 0 par "wall" et mettre sprite au pluriel pour montrer que c'est un tableau
          # modifier 1 par "path"           


       



