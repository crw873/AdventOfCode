# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/8/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Read the data into an np.array 
raw_input_list = response.text.split('\n')
input_list = [list(tree_str) for tree_str in raw_input_list if tree_str != '']
input_array = np.array(input_list, dtype=int)

# %%

# Set up a matrix for the visible trees 
visible_trees = np.zeros(input_array.shape)

def check_visible_tree(matrix, row, col):
    # Return visible if on the outside 
    if row == 0 or row == matrix.shape[0]-1: return 1
    if col == 0 or col == matrix.shape[1]-1: return 1

    # Get the size of the tree in question 
    tree_size = matrix[row, col]

    # Check Visible from top
    if tree_size > matrix[:row, col].max(): return 1

    # Check Visible from bottom
    if tree_size > matrix[row+1:, col].max(): return 1

    # Check Visible from left
    if tree_size > matrix[row, :col].max(): return 1

    # Check Visible from right
    if tree_size > matrix[row, col+1:].max(): return 1

    # Return 0 if not visible from any other side 
    return 0

for row in range(input_array.shape[0]):
    for col in range(input_array.shape[1]):
        visible_trees[row, col] = check_visible_tree(input_array, row, col)

visible_trees.sum()

# %%
