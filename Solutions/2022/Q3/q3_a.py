# %%

# General Imports 
import requests
import pandas as pd
from io import StringIO

# %%

# Puzzle Input URL
url = 'https://adventofcode.com/2022/day/3/input'

# Get the data 
SESSIONID = open('session_id.txt').read()
USER_AGENT = 'crw873'

# Cache the response if already got 
response = requests.get(url, cookies={'session': SESSIONID}, headers={'User-Agent': USER_AGENT})

# %%

# Format the data 
df = pd.read_csv(StringIO(response.text), skip_blank_lines=False, names=['items']).fillna(0)#.astype({'Calories':int})

char_str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
score_lookup_dict = {c:n for c,n in zip(char_str, range(1, 53))}

def get_score(x):
    size_of_rucksack = len(x)
    rucksack1 = x[:size_of_rucksack//2]
    rucksack2 = x[size_of_rucksack//2:]
    item = min(set(rucksack1).intersection(rucksack2))
    return score_lookup_dict[item]

df['Score'] = df['items'].apply(lambda x: get_score(x))
df.sum()

# %%
