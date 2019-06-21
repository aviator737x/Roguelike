from MapObjects.Character.Mob import *
from MapObjects.Character.ConfusionDecorator import *
from MapObjects.Inventory.UpgradeAttack import *
from MapObjects.Inventory.UpgradeHealth import *
from MapObjects.Inventory.UpgradeBoth import *
from Window.GameMap import *
from Window.BackpackWindow import *


class Environment:
    def __init__(self, map_grid):
        rnd.seed()
        self.map = GameMap(map_grid)
        self.symbols_on_map = {
            b'.': '.',
            b'#': '#'
        }
        self.window = self.map
        self.player = Player()
        self.position_map_object(self.player)
        self.mobs = set()
        self.map.draw()

    def initFromFile(self, file_name):
        with open(file_name) as file:
            height = file.readline()
            width = file.readline()
            map_grid = np.chararray(shape=(int(height), int(width)))
            map_grid[:] = '.'
            self.map = GameMap(map_grid)
            self.symbols_on_map = {
                b'.': '.',
                b'#': '#'
            }
            cells = self.map.cells
            self.window = self.map
            self.mobs = set()
            counter = 0
            for row in range(len(map_grid)):
                for column in range(len(map_grid[0])):
                    counter += 1
                    cell = cells[row][column]
                    line = file.readline()
                    if line == '#\n':
                        cell.is_wall = True
                        cell.free_to_move = False
                        cell.is_empty = False
                        continue
                    if line == '.\n':
                        continue
                    if line == '(\n':
                        inventory = UpgradeAttack()
                        cell.set_object(inventory)
                        continue
                    if line == ')\n':
                        inventory = UpgradeHealth()
                        cell.set_object(inventory)
                        continue
                    if line == '?\n':
                        inventory = UpgradeBoth()
                        cell.set_object(inventory)
                        continue
                    if line == '@\n':
                        self.player = Player()
                        character = self.player
                    elif line == '%\n':
                        character = Mob(0)
                        self.mobs.add(character)
                    elif line == '*\n':
                        character = Mob(1)
                        self.mobs.add(character)
                    elif line == '\n':
                        continue
                    else:
                        character = Mob(2)
                        self.mobs.add(character)
                    character.set_position(column, row)
                    line = file.readline()
                    character.health = int(line[:-1])
                    character.attack = int(file.readline()[:-1])
                    file.readline()
                    line = file.readline()
                    if line == "Attack updater (w/s)\n":
                        num = int(file.readline()[:-1])
                        character.backpack["Attack updater (w/s)"] = []
                        for _ in range(num):
                            character.backpack["Attack updater (w/s)"].append(UpgradeAttack())
                        line = file.readline()
                    if line == "Health upgrader (e/d)\n":
                        num = int(file.readline()[:-1])
                        character.backpack["Health upgrader (e/d)"] = []
                        for _ in range(num):
                            character.backpack["Health upgrader (e/d)"].append(UpgradeAttack())
                        line = file.readline()
                    if line == "A/H upgrader (r/f)\n":
                        num = int(file.readline()[:-1])
                        character.backpack["A/H upgrader (r/f)"] = []
                        for _ in range(num):
                            character.backpack["A/H upgrader (r/f)"].append(UpgradeAttack())
                        line = file.readline()
                    line = file.readline()
                    if line == "Attack updater (w/s)\n":
                        num = int(file.readline()[:-1])
                        character.worn["Attack updater (w/s)"] = []
                        for _ in range(num):
                            character.worn["Attack updater (w/s)"].append(UpgradeAttack())
                        line = file.readline()
                    if line == "Health upgrader (e/d)\n":
                        num = int(file.readline()[:-1])
                        character.worn["Health upgrader (e/d)"] = []
                        for _ in range(num):
                            character.worn["Health upgrader (e/d)"].append(UpgradeAttack())
                        line = file.readline()
                    if line == "A/H upgrader (r/f)\n":
                        num = int(file.readline()[:-1])
                        character.worn["A/H upgrader (r/f)"] = []
                        for _ in range(num):
                            character.worn["A/H upgrader (r/f)"].append(UpgradeAttack())
                        line = file.readline()
                    if isinstance(character, Player):
                        character.wins_on_level = int(line[:-1])
                        line = file.readline()
                        character.level = int(line[:-1])
        self.map.draw()

    def check_uncheck_backpack(self):
        if self.window == self.map:
            self.window = BackpackWindow(self.map.cells.shape)
            self.window.set_backpack(self.player.backpack)
        else:
            self.window = self.map

    def position_map_object(self, map_object):
        empty_cells = np.where(self.map.window == b'.')
        num_of_empty_cells = len(empty_cells[0])
        cell_to_place = rnd.randrange(0, num_of_empty_cells)
        y = empty_cells[0][cell_to_place]
        x = empty_cells[1][cell_to_place]
        self.map.set_object(map_object, y, x)
        self.symbols_on_map[map_object.array_symbol] = map_object.symbol
        map_object.set_position(x, y)

    def confuse_player(self):
        self.player = ConfusionDecorator(self.player, 10)

    # random mob creation here
    def before_update(self):
        rand_number = rnd.randint(1, 50)
        if rand_number == 1:
            self.confuse_player()
        rand_number = rnd.randint(1, 20)
        if rand_number == 1:
            rand_strategy = rnd.randint(0, 2)
            mob = Mob(rand_strategy)
            self.position_map_object(mob)
            self.mobs.add(mob)
        rand_number = rnd.randint(1, 50)
        inventory = None
        if rand_number == 1:
            inventory = UpgradeAttack()
        if rand_number == 2:
            inventory = UpgradeHealth()
        if rand_number == 3:
            inventory = UpgradeBoth()
        if inventory is not None:
            self.position_map_object(inventory)
        if rand_number < 10:
            for mob in self.mobs:
                mob.wear_from_backpack("Attack updater (w/s)")
        elif rand_number < 20:
            for mob in self.mobs:
                mob.wear_from_backpack("Health upgrader (e/d)")
        elif rand_number < 30:
            for mob in self.mobs:
                mob.wear_from_backpack("A/H upgrader (r/f)")
        elif rand_number == 49:
            for mob in self.mobs:
                mob.take_of("Attack updater (w/s)")
        elif rand_number == 48:
            for mob in self.mobs:
                mob.take_of("Health upgrader (e/d)")
        elif rand_number == 47:
            for mob in self.mobs:
                mob.take_of("A/H upgrader (r/f)")

    def update(self, direction):
        if self.map != self.window:
            return 0
        self.before_update()
        new_map = [[set() for _ in range(len(self.map.cells[i]))] for i in range(len(self.map.cells))]
        for mob in self.mobs:
            new_x, new_y = mob.get_desired_position(self.map.cells, (self.player.x, self.player.y))
            new_map[new_y][new_x].add(mob)
        new_x, new_y = self.player.get_desired_position(self.map.cells, direction)
        new_map[new_y][new_x].add(self.player)
        resolve_collisions = True
        while resolve_collisions:
            resolve_collisions = False
            for row in range(len(new_map)):
                for column in range(len(new_map[0])):
                    if len(new_map[row][column]) > 1:  # more than one character tries to place cell
                        fighters = new_map[row][column]
                        loosers = Character.battle(fighters)
                        if self.player in fighters:
                            self.player.wins_on_level += len(loosers)
                            if self.player.wins_on_level > 20:
                                self.player.upgrade_level()
                        if loosers:
                            for looser in loosers:
                                if looser == self.player:
                                    return 1
                                self.mobs.remove(looser)
                                fighters.remove(looser)

                        if not loosers or len(fighters) > 1:
                            resolve_collisions = True
                            for fighter in fighters:
                                new_map[fighter.y][fighter.x].add(fighter)
                            new_map[row][column].clear()

        for row in range(len(new_map)):
            for column in range(len(new_map[0])):
                cell = self.map.cells[row][column]
                if new_map[row][column]:
                    character = new_map[row][column].pop()
                    if isinstance(cell.map_object, Inventory):
                        character.add_to_backpack(cell.map_object)
                    self.map.set_object(character, row, column)
                    character.set_position(column, row)
                elif not isinstance(cell.map_object, Inventory) and not cell.is_wall:
                    self.map.clear_cell(row, column)
        self.map.draw()

        return 0

    def write_to_file(self, file_name):
        with open(file_name, "w") as file:
            file.write(str(len(self.map.cells)) + "\n")
            file.write(str(len(self.map.cells[0])) + "\n")
            for row in range(len(self.map.cells)):
                for column in range(len(self.map.cells[row])):
                    cell = self.map.cells[row][column]
                    if cell.is_wall:
                        file.write("#\n")
                        continue
                    if cell.is_empty:
                        file.write(".\n")
                        continue
                    map_object = cell.map_object
                    file.write(map_object.symbol + "\n")
                    if isinstance(map_object, Character):
                        file.write(str(map_object.health) + "\n")
                        file.write(str(map_object.attack) + "\n")
                        file.write("Backpack:" + "\n")
                        if "Attack updater (w/s)" in map_object.backpack:
                            file.write("Attack updater (w/s)\n" + str(len(map_object.backpack["Attack updater (w/s)"])) + "\n")
                        if "Health upgrader (e/d)" in map_object.backpack:
                            file.write("Health upgrader (e/d)\n" + str(len(map_object.backpack["Health upgrader (e/d)"])) + "\n")
                        if "A/H upgrader (r/f)" in map_object.backpack:
                            file.write("A/H upgrader (r/f)\n" + str(len(map_object.backpack["A/H upgrader (r/f)"])) + "\n")
                        file.write("Worn:" + "\n")
                        if "Attack updater (w/s)" in map_object.worn:
                            file.write("Attack updater (w/s)\n" + str(len(map_object.worn["Attack updater (w/s)"])) + "\n")
                        if "Health upgrader (e/d)" in map_object.worn:
                            file.write("Health upgrader (e/d)\n" + str(len(map_object.worn["Health upgrader (e/d)"])) + "\n")
                        if "A/H upgrader (r/f)" in map_object.worn:
                            file.write("A/H upgrader (r/f)\n" + str(len(map_object.worn["A/H upgrader (r/f)"])) + "\n")
                    if isinstance(map_object, Player):
                        file.write(str(map_object.wins_on_level) + "\n")
                        file.write(str(map_object.level) + "\n")
                    else:
                        file.write('\n')
