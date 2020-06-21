class colors:
    black = "\033[0;30m"
    red = "\033[0;31m"
    green = "\033[0;32m"
    yellow = "\033[0;33m"
    blue = "\033[0;34m"
    magenta = "\033[0;35m"
    cyan = "\033[0;36m"
    white = "\033[0;37m"
    bright_black = "\033[0;90m"
    bright_red = "\033[0;91m"
    bright_green = "\033[0;92m"
    bright_yellow = "\033[0;93m"
    bright_blue = "\033[0;94m"
    bright_magenta = "\033[0;95m"
    bright_cyan = "\033[0;96m"
    bright_white = "\033[0;97m"

ver = 1
name = "8BP"

import time
import sys
import curses
import os
from random import randint, choice
import random
from termcolor import cprint
import time

nums = [
    0,
    10,
    20,
    40,
    60,
    90,
    99,
    100
]

def clear():
  curses.setupterm()
  e3 = curses.tigetstr('E3') or b''
  clear_screen_seq = curses.tigetstr('clear') or b''
  os.write(sys.stdout.fileno(), e3 + clear_screen_seq)

for i in range(10):
    time.sleep(1)
    num = i * 10
    print(f"{name} {ver} | The Virtual Game Console")
    print(f"Loading... {num}%")
    time.sleep(1)
    clear()



print(f"WELCOME TO {name} {ver}!")

press_any_key = input("PRESS ANY KEY\n")
clear()
print(f"{name} {ver} | The Virtual Game Console")
game = input("Would you like to choose a game? (Y/N)\n>>>")

f=open("catalog.txt", "r")

catalog = f.read()

if game.find("y") != -1:
    clear()
    time.sleep(1.86965754)
    print(f"{name} {ver} | The Virtual Game Console | Catalog")
    selection = input(f"{catalog}\nType in the number that corresponds with the game you want to play\n>>>")
    if selection == 1 or selection == "1":
        clear()
        exec(open("games/droids/droids.py").read())
        