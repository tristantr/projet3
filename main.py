import logic
from logic import characters
from logic import stage

 
MacGyver = characters.Hero(3,0)
MacGyver.print()
Labyrinth = stage.Stage('Map/map1.txt')
Labyrinth.generate()
