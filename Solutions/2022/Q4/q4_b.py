# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/4/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['elf1', 'elf2'])

def get_min_max(x):
    elf1_min, elf1_max = x.elf1.split('-')
    elf2_min, elf2_max = x.elf2.split('-')

    # Convert types
    elf1_min = int(elf1_min)
    elf2_min = int(elf2_min)
    elf1_max = int(elf1_max)
    elf2_max = int(elf2_max)

    # Check if one group engulfs the other group
    if elf1_min > elf2_max: return 0
    if elf1_max < elf2_min: return 0
    return 1

df['Score'] = df.apply(lambda x: get_min_max(x), axis=1)
df.sum()

# %%
