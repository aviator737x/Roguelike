from MapGenerator import *
from MapLoader import *
from InputHandler import *
from Environment import *

import os


if os.path.exists("saved_game.txt"):
    print("Generate map - 1, load map - 2, load saved game - 3")
else:
    print("Generate map - 1, load map - 2")

s = input()
game_map = None

if s == "1":
    print("Enter size of map")
    size = int(input())
    map_generator = MapGenerator(size)
    game_map = map_generator.generate_map()
elif s == "2":
    print("Enter path to the map")
    path = input()
    game_map = MapLoader(path)
elif s == "3" and os.path.exists("saved_game.txt"):
    map_generator = MapGenerator(10)
    game_map = map_generator.generate_map()

environment = Environment(game_map)
if s == "3" and os.path.exists("saved_game.txt"):
    environment.initFromFile("saved_game.txt")
input_handler = InputHandler(environment)
