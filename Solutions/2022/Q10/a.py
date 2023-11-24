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
raw_input_list

# %%

# Set starting values 
cycles = [1,1]

for instruction in raw_input_list:
    print(instruction)
    cycles.append(cycles[-1])
    if instruction.startswith('addx'): 
        action, value = instruction.split(' ')
        cycles.append(cycles[-1] + int(value))

signal_strengths = [i*cycles[i] for i in range(20, 221, 40)]
np.sum(signal_strengths)

# %%
