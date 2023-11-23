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
start_position = np.array([0,0])
rope_pieces = [i for i in range(0,10)]
rope_positions = {piece: start_position.copy() for piece in rope_pieces}

# Set the current state 
t_possitions = [str(start_position)]

for input in raw_input_list[:-1]:
    print(input)
    move, steps = input.split(' ')
    for i in range(int(steps)):
        # Move H
        rope_positions[0] += move_actions[move]

        # Work out where T goes 
        for rope in range(1,10): 
            relative_position = rope_positions[rope-1] - rope_positions[rope]
            if max(abs(relative_position)) >= 2:  
                rope_positions[rope] += np.sign(relative_position)

            print(rope_positions[0], rope_positions[9], relative_position)

        # Save spaces 
        t_possitions.append(str(rope_positions[rope]))

            # print(i, rope_positions[rope])

len(set(t_possitions))

# %%