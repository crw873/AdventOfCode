# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/2/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['Play']).fillna(0)#.astype({'Calories':int})

# Points look up table 
point_lookup_table = {
    # Single score
    'X': 1,
    'Y': 2,
    'Z': 3,

    # Joint score
    'A X': 3,
    'B X': 1,
    'C X': 2,
    'A Y': 4,
    'B Y': 5,
    'C Y': 6,
    'A Z': 8,
    'B Z': 9,
    'C Z': 7,
}

df['Score'] = df['Play'].apply(lambda x: point_lookup_table[x])
df.sum()

# %%
