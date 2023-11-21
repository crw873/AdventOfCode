# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/5/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Inital Set up visual (copy paste from browser) 
# [M]                     [N] [Z]    
# [F]             [R] [Z] [C] [C]    
# [C]     [V]     [L] [N] [G] [V]    
# [W]     [L]     [T] [H] [V] [F] [H]
# [T]     [T] [W] [F] [B] [P] [J] [L]
# [D] [L] [H] [J] [C] [G] [S] [R] [M]
# [L] [B] [C] [P] [S] [D] [M] [Q] [P]
# [B] [N] [J] [S] [Z] [W] [F] [W] [R]

# Format the data 
df = pd.read_csv(
    StringIO(response.text), 
    skip_blank_lines=False, 
    names=['Instructions'], 
    skiprows=10 # We need to skip the part with the initial set up 
)

class Crane():
    def __init__(self, response):
        # Parse the raw csv from the api call
        initial_set_up_raw = response.text.split('\n')[:8]

        # Create the list of list that represent the initial set up of the boxes
        self.set_up = {stack+1:[initial_set_up_raw[row][i] for row in range(8) if initial_set_up_raw[row][i] != ' '][::-1] for stack, i in enumerate(range(1,35,4))}

    def move_boxes(self, nboxes, from_row, to_row):
        # Get the boxes htat need to move 
        boxes_to_move = self.set_up[from_row][-1*nboxes:]

        # remove these boxes from the relevant pile
        del self.set_up[from_row][-1*nboxes:]

        # Add the boxes to the relevant pile
        self.set_up[to_row].extend(boxes_to_move)

    def get_top_layer(self):
        top_layer_list = [row[-1] for row in self.set_up.values()]
        return ''.join(top_layer_list)

def get_parameters_to_move_box(x, active_crane):
    # split the string to get an easy way of collecting parameters
    instructions = x.split(' ')

    # Collect the parameter
    nboxes = int(instructions[1])
    from_row = int(instructions[3])
    to_row = int(instructions[5])

    # Perform the box move
    active_crane.move_boxes(nboxes, from_row, to_row)

    return x

# Set up the crane 
active_crane = Crane(response)

# Iterate through instructions omving the boxes accordingly 
df['Instructions'].apply(lambda x: get_parameters_to_move_box(x, active_crane))
# active_crane.set_up
active_crane.get_top_layer()

# Move the boxes 


# %%
