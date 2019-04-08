from asciimatics.screen import Screen
import curses
from MapGenerator import *
from MapLoader import *



def func(map = None):

    def demo(screen):
        j = 0
        x = 0
        y = 0
        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == b'.':
                    screen.print_at('.', i, j)
                    x = i
                    y = j
                else:
                    screen.print_at('#', i, j)
        screen.print_at('@', x, y)
        screen.refresh()
        try:
            while True:
                stdscr = curses.initscr()
                curses.noecho()
                curses.cbreak()
                stdscr.keypad(1)
                key = stdscr.getch()
                if key == 259 and y > 0 and map[x][y-1] != b'#':
                    screen.print_at('.', x, y)
                    y -= 1
                    screen.print_at('@', x, y)
                    screen.refresh()
                if key == 258 and y < len(map[0]) - 1 and map[x][y+1] != b'#':
                    screen.print_at('.', x, y)
                    y += 1
                    screen.print_at('@', x, y)
                    screen.refresh()
                if key == 261 and x < len(map) - 1 and map[x+1][y] != b'#':
                    screen.print_at('.', x, y)
                    x += 1
                    screen.print_at('@', x, y)
                    screen.refresh()
                if key == 260 and x > 0 and map[x-1][y] != b'#':
                    screen.print_at('.', x, y)
                    x -= 1
                    screen.print_at('@', x, y)
                    screen.refresh()
        except KeyboardInterrupt:
            exit(0)

    return demo



print("Generate map - 1, load map - 2")
s = input()
if s == "1":
    print("Enter size of map")
    size = int(input())
    map = MapGenerator(size)
    Screen.wrapper(func(map.generate_map()))
elif s == "2":
    print("Enter path to the map")
    path = input()
    map = MapLoader(path)
    Screen.wrapper(func(map.generate_map()))


