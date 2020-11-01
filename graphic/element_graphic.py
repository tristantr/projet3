class ElementDisplay:
    """
    Superclass of the graphic part 

    """	

    def __init__(self, screenDisplay, personnageDisplay, stageDisplay, itemsDisplay):
        """
        Init method for the ElementDisplay class

        Parameters
        ----------
        screenDisplay : obj
            From ScreenDisplay class in screen_graphic.py
            
        personnageDisplay : obj
            From PersonnageDisplay class in characters_graphic.py
            
        stageDisplay : obj
            From StageDisplay class in stage_graphic.py

        itemsDisplay : obj
            From ItemsDisplay class in items_graphic.py
           
        """    	
        self.screenDisplay = screenDisplay
        self.personnageDisplay = personnageDisplay
        self.stageDisplay = stageDisplay
        self.itemsDisplay = itemsDisplay

class ElementDisplay:

    def __init__(self, screenDisplay, personnageDisplay, stageDisplay, itemsDisplay):   
        self.screenDisplay = screenDisplay
        self.personnageDisplay = personnageDisplay
        self.stageDisplay = stageDisplay
        self.itemsDisplay = itemsDisplay