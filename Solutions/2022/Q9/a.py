# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/9/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Read the data into an np.array 
raw_input_list = response.text.split('\n')
raw_input_list
# input_list = [list(tree_str) for tree_str in raw_input_list if tree_str != '']
# input_array = np.array(input_list, dtype=int)

# %%

move_actions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1,0)
}

# Get the stating positions  
hpos = np.array([0,0])
tpos = np.array([0,0])

# Set the current state 
t_possitions = [str(tpos)]

for input in raw_input_list[:-1]:
    print(input)
    move, steps = input.split(' ')
    for i in range(int(steps)):
        # Move H
        hpos += move_actions[move]

        # Work out where T goes 
        relative_position = hpos - tpos
        if max(abs(relative_position)) >= 2:  
            tpos += np.sign(relative_position)

        # Save spaces 
        t_possitions.append(str(tpos))
        print(hpos, tpos, relative_position)

len(set(t_possitions))

# %%