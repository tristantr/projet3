from . import constants


class Stage:

    """
    Create a stage

    """    
    def __init__(self, file):
        """
        Init method for the Stage class

        Parameters
        ----------
        file : str
            Txt File from the Map directory
        """   

        self.file = file
        self.sprites_for_walls = []
        self.sprites_for_path = []
        self.index_first_sprite = 0
        self.index_last_sprite_of_a_line = 14
        self.index_last_sprite = 224
        self._create_coordonates()
        self.generate()

    def _create_coordonates(self):

        """
        Generate the list of our stage possible coordonates 

        Returns
        -------
        list
            Coordonates 


        """   

        self.coordonates = []

        for j in range(self.index_first_sprite, self.index_last_sprite_of_a_line + 1):
            for i in range(self.index_first_sprite, self.index_last_sprite_of_a_line + 1):
                self.coordonates.append(
                    [i * constants.SPRITE_SIZE, j * constants.SPRITE_SIZE])        

    def generate(self):
        """
        Read the Map file and create lists of sprites for wall and sprite for path coordonates

        Returns
        -------
        lists
            Sprites_for_wall[]
            Sprites_for_path[]

        """

        file = open(str(self.file))
        read_file = file.read()
        Map = read_file.split()
        value_for_wall = 0

        for i in range(self.index_first_sprite, self.index_last_sprite + 1):
            if Map[i] == str(value_for_wall):
                self.sprites_for_walls.append(self.coordonates[i])
            else:
                self.sprites_for_path.append(self.coordonates[i])

    def get_sprites_for_path(self):
        """
        Get method to get sprites_for_path[]

        """
        return self.sprites_for_path

