from logic import constants

class Character:

    """
    Mother-class: Create a character

    """

    def __init__(self, x, y, image):

        """
        Init method for the Character class

        Parameters
        ----------
        x : int
            Character sprite abscissa (between 0 and 14)
        y : int
            character sprite ordinate (between 0 and 14)
        image : string
            character image

        """

        self.x = x * constants.SPRITE_SIZE
        self.y = y * constants.SPRITE_SIZE
        self.image = image


class Hero(Character):

    """
    Descendant class from Character class: Create the game hero

    """    

    def __init__(self, x, y, image):

        """
        Parameters
        ----------
        x : int
            Hero sprite abscissa (between 0 and 14)
        y : int
            Hero sprite ordinate (between 0 and 14)
        image : string
            Hero image

        """
        super().__init__(x, y, image)

    def go_up(self):

        """
        Move the hero 40 pxl up

        """
        self.y -= constants.SPRITE_SIZE

    def go_down(self):

        """
        Move the hero 40 pxl down

        """    
        self.y += constants.SPRITE_SIZE

    def go_right(self):

        """
        Move the hero 40 pxl right

        """
        self.x += constants.SPRITE_SIZE

    def go_left(self):
    
        """
        Move the hero 40 pxl left

        """
        self.x -= constants.SPRITE_SIZE

    def get_x(self):
    
        """
        Returns the hero abscissa

        """  
        return self.x

    def get_y(self):

        """
        Returns the hero ordonate

        """
        return self.y


class Ennemy(Character):

    """
    Descendant class from Character class: Create the game hero

    """  

    def __init__(self, x, y, image):

        """
        Parameters
        ----------
        x : int
            Hero sprite abscissa (between 0 and 14)
        y : int
            Hero sprite ordinate (between 0 and 14)
        image : string
            Hero image

        """ 
        super().__init__(x, y, image)