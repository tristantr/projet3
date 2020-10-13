SPRITE_SIZE = 40

      
### LOGIQUE ###      

#sprites_for_wall = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 0
#sprites_for_path = [] # On créé un tableau avec les coordonnées des élements associés à la valeur 1

class Stage:
    def __init__(self, file):
        self.file = file
        self.sprites_for_walls = []
        self.sprites_for_path = []
        self.index_first_sprite = 0
        self.index_last_line_sprite = 14
        self.index_last_sprite = 224
        self._create_coordonates()

    def _create_coordonates(self):
        self.coordonates = []

        for j in range(self.index_first_sprite, self.index_last_line_sprite + 1):                      
            for i in range (self.index_first_sprite, self.index_last_line_sprite + 1):                 
                self.coordonates.append([i * SPRITE_SIZE, j * SPRITE_SIZE]) 


    def generate(self):

        file = open(str(self.file))
        read_file = file.read()
        Map = read_file.split()
        value_for_wall = 0
            
        for i in range(self.index_first_sprite,self.index_last_sprite + 1):
        # Si la valeur dans Map vaut 0, on ajoute le couple de coordonnées du tableau Coordonates au même index à sprites_for_walls    
            if Map[i] == str(value_for_wall):        
                self.sprites_for_walls.append(self.coordonates[i])  
            else:
        # Si la valeur dans Map vaut 1, on ajoute le couple de coordonnées du tableau Coordonates au même index à Sprites_for_path            
                self.sprites_for_path.append(self.coordonates[i])   
                      
    def get_arrays(self):
        return self.sprites_for_path                

       



