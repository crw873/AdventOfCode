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

def get_direction_scores(matrix, row, col):
    # Set row and col lengths
    nrows, ncols = matrix.shape

    # Set the direction scores list
    direction_scores = {
        'up': 0,
        'down': 0,
        'left': 0,
        'right': 0
    }

    # Get the size of the tree in question 
    tree_size = matrix[row, col]

    # Check Visible to top
    if row == 0:
        direction_scores['up'] = 0
    else: 
        for tree_count, tree in enumerate(matrix[:row, col][::-1], start=1):
            print(tree)
            if tree >= tree_size:
                direction_scores['up'] = tree_count
                break
            direction_scores['up'] = tree_count

    # Check Visible to bottom
    if row == matrix.shape[0]:
        direction_scores['down'] = 0
    else: 
        for tree_count, tree in enumerate(matrix[row+1:, col], start=1):
            print(tree)
            if tree >= tree_size:
                direction_scores['down'] = tree_count
                break
            direction_scores['down'] = tree_count

    # Check Visible to left
    if col == 0:
        direction_scores['left'] = 0
    else: 
        for tree_count, tree in enumerate(matrix[row, :col][::-1], start=1):
            print(tree)
            if tree >= tree_size:
                direction_scores['left'] = tree_count
                break
            direction_scores['left'] = tree_count

    # Check Visible to right
    if row == matrix.shape[0]:
        direction_scores['right'] = 0
    else: 
        for tree_count, tree in enumerate(matrix[row, col+1:], start=1):
            print(tree)
            if tree >= tree_size:
                direction_scores['right'] = tree_count
                break
            direction_scores['right'] = tree_count

    # Return 0 if not visible from any other side 
    return direction_scores 

for row in range(input_array.shape[0]):
    for col in range(input_array.shape[1]):
        direction_scores = get_direction_scores(input_array, row, col)
        visible_trees[row, col] = np.prod(list(direction_scores.values()))

visible_trees.max()
# %%
