class Element:
    """
    Superclass of the logic part 

    """
    def __init__(self, hero, ennemy, stage, items):
    
        """
        Init method for the Element class

        Parameters
        ----------
        hero : obj
            From Hero(Character) class in characters.py
            
        ennemy : obj
            From Ennemy(Character) class in characters.py
            
        stage : obj
            From Stage class in stage.py

        items : obj
            From Items class in items.py
           
        """

        self.hero = hero
        self.ennemy = ennemy
        self.stage = stage
        self.items = items