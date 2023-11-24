# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/10/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Read the data into an np.array 
raw_input_list = response.text.split('\n')[:-1]

# %%

# Set up the screen output 
graphic = np.zeros(6*40, dtype=str)

# Set starting values 
cycles = [0]

def get_graphic_value(cycle_number, xpos):
    if abs(((cycle_number) % 40) - xpos) <= 1:
        return '#'
    return '.'


for instruction in raw_input_list:
    cycle_number = len(cycles)-2
    print(cycle_number)
    graphic[cycle_number] = get_graphic_value(cycle_number, cycles[-1])
    cycles.append(cycles[-1])
    if instruction.startswith('addx'): 
        action, value = instruction.split(' ')
        cycle_number = len(cycles)-2
        graphic[cycle_number] = get_graphic_value(cycle_number, cycles[-1])
        cycles.append(cycles[-1] + int(value))

graphic.reshape([6,40])[::-1].T
# %%
