import logic
from logic import characters
from logic import stage

import display

 
MacGyver = characters.Hero(3,0)
Labyrinth = stage.Stage('Map/map1.txt')
Labyrinth.generate()


