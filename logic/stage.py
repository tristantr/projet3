from . import constants
      
class Stage:
    def __init__(self, file):
        self.file = file
        self.sprites_for_walls = []
        self.sprites_for_path = []
        self.index_first_sprite = 0
        self.index_last_line_sprite = 14
        self.index_last_sprite = 224
        self._create_coordonates()
        self._generate()

    def _create_coordonates(self):
        self.coordonates = []

        for j in range(self.index_first_sprite, self.index_last_line_sprite + 1):                      
            for i in range (self.index_first_sprite, self.index_last_line_sprite + 1):                 
                self.coordonates.append([i * constants.SPRITE_SIZE, j * constants.SPRITE_SIZE]) 


    def _generate(self):

        file = open(str(self.file))
        read_file = file.read()
        Map = read_file.split()
        value_for_wall = 0
            
        for i in range(self.index_first_sprite,self.index_last_sprite + 1):   
            if Map[i] == str(value_for_wall):        
                self.sprites_for_walls.append(self.coordonates[i])  
            else:           
                self.sprites_for_path.append(self.coordonates[i])   
                      
    def get_sprites_for_path(self):
        return self.sprites_for_path  

    def get_sprites_for_wall(self):
        return self.sprites_for_walls                  

#labyrinth = Stage('Map/map1.txt')
      



