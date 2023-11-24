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

# 55

correct_order_indices = []

def comp_list_lengths(left_raw, right_raw, i):
    left = left_raw.copy()
    right = right_raw.copy()

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
    left = eval(left)
    right = eval(right)
    order = comp_list_lengths(left, right, i)
    correct_order_indices.append(order) 

np.sum(correct_order_indices)

# %%

input_data2 = [eval(packet) for packet in input_data if packet != ''] + [[[2]]] + [[[6]]]
input_data2

nchanges = 1
n = len(input_data2)
icount = 0

while nchanges > 0:
    nchanges = 0
    new_sorted_list = []
    current_highest = input_data2[0].copy()
    for i in range(n-1): 
        test_highest = input_data2[i+1].copy()
        comp = comp_list_lengths(current_highest, test_highest, 1)
        if comp > 0:
            new_sorted_list.append(current_highest)
            current_highest = test_highest.copy()
        else:
            new_sorted_list.append(test_highest)
            nchanges += 1
    new_sorted_list.append(current_highest)
    input_data2 = new_sorted_list.copy() 

    icount += 1
    print(icount)
    
    if icount == 1000: break

sorted_dict = {i:val for i, val in enumerate(new_sorted_list, start=1) if val in [[[6]], [[2]]]}
np.prod(list(sorted_dict.keys()))
# for i, val in sorted_dict.items():
#     if val == [[2]]:
#         print(i, val)
#     if val == [[6]]:
#         print(i, val)

# %%
