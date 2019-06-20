from MapGenerator import *
from MapLoader import *
from InputHandler import *
from Environment import *


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
environment = Environment(game_map)
input_handler = InputHandler(environment)
