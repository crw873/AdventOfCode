# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO
import numpy as np

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/13/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

input_data = response.text.split('\n')

correct_order_indices = []

def comp_list_lengths(left, right, i):
    print(left, right)
    # Check if one is empty
    if len(left) == 0 or len(right) == 0:
        return i*(len(left) == 0)
        correct_order_indices.append(len(l) == 0)

    # Get the first index in the list
    l = left[0]
    r = right[0]

    # If the list are the same continue recursion
    if l == r: return comp_list_lengths(left[1:], right[1:], i)

    # Check if the imputs are both integers 
    if type(l) == int and type(r) == int: 
        return i*(l < r)
        correct_order_indices.append(i*(l < r))

    # if not make them both lists
    if type(l) == int: l = [l]
    if type(r) == int: r = [r]

    return comp_list_lengths(l, r, i)

for i, left, right in zip(range(1,len(input_data)), input_data[::3], input_data[1::3]):
    print(i)
    left = eval(left)
    right = eval(right)
    order = comp_list_lengths(left, right, i)
    print(order)
    correct_order_indices.append(order) 

np.sum(correct_order_indices)

# %%